#!/usr/bin/env bash
#
# pandoc-watch.command
# -------------------------------------------------------------------
# Drop Markdown (.md / .markdown) files into the "inbox" folder and
# this script auto-converts each one to DOCX in "output".
# Originals are moved to "processed" so the inbox stays clean.
#
# Mermaid support (added 2026-07-24):
#   ```mermaid code blocks are rendered as diagrams in the DOCX when
#   mermaid-filter is installed:  npm install -g mermaid-filter
#   Without it, files still convert; diagrams appear as code blocks.
#
# Usage:
#   * Double-click this file in Finder, OR
#   * Run it from Terminal:  ./pandoc-watch.command
#   Press Ctrl-C (or close the window) to stop watching.
# -------------------------------------------------------------------

set -u

# --- Locate this script's folder (handles spaces in the path) -------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

INBOX="$SCRIPT_DIR/inbox"
OUTPUT="$SCRIPT_DIR/output"
PROCESSED="$SCRIPT_DIR/processed"
REFERENCE="$SCRIPT_DIR/Pandoc_Ref.docx"
POLL_SECONDS=2

mkdir -p "$INBOX" "$OUTPUT" "$PROCESSED"

# --- Use the reference doc for styling if it exists -----------------
REF_ARGS=()
if [ -f "$REFERENCE" ]; then
  REF_ARGS=(--reference-doc="$REFERENCE")
fi

# --- Check pandoc is installed --------------------------------------
if ! command -v pandoc >/dev/null 2>&1; then
  echo "ERROR: pandoc is not installed or not on your PATH."
  echo "Install it with:  brew install pandoc"
  echo
  read -r -p "Press Return to close." _ || true
  exit 1
fi

# --- Mermaid rendering (optional) -----------------------------------
# mermaid-filter renders ```mermaid blocks into PNG images inside the
# DOCX. Settings below control output quality and appearance.
HAVE_MERMAID=0
if command -v mermaid-filter >/dev/null 2>&1; then
  HAVE_MERMAID=1
  export MERMAID_FILTER_FORMAT=png
  export MERMAID_FILTER_BACKGROUND=white
  export MERMAID_FILTER_SCALE=2
fi

echo "=================================================="
echo " Pandoc watch folder (Markdown -> DOCX)"
echo "=================================================="
echo " Drop .md files into : $INBOX"
echo " Results appear in   : $OUTPUT"
echo " Originals move to   : $PROCESSED"
if [ ${#REF_ARGS[@]} -gt 0 ]; then
  echo " Style reference     : $(basename "$REFERENCE")"
else
  echo " Style reference     : none (drop Pandoc_Ref.docx here to enable)"
fi
if [ "$HAVE_MERMAID" -eq 1 ]; then
  echo " Mermaid diagrams    : rendered (mermaid-filter found)"
else
  echo " Mermaid diagrams    : NOT rendered (install: npm install -g mermaid-filter)"
fi
echo " Checking every ${POLL_SECONDS}s.  Press Ctrl-C to stop."
echo "=================================================="
echo

# --- Convert a single markdown file ---------------------------------
convert_file() {
  local src="$1"
  local base name
  base="$(basename "$src")"
  name="${base%.*}"

  echo "[$(date '+%H:%M:%S')] Converting: $base"

  # Apply the mermaid filter only when the file contains mermaid blocks
  local filter_args=()
  if grep -q '^[[:space:]]*```mermaid' "$src"; then
    if [ "$HAVE_MERMAID" -eq 1 ]; then
      filter_args=(-F mermaid-filter)
      echo "    (mermaid blocks detected -> rendering diagrams)"
    else
      echo "    !! Mermaid blocks found but mermaid-filter is not installed."
      echo "       Diagrams will appear as code. Install: npm install -g mermaid-filter"
    fi
  fi

  # Note: ${arr[@]+...} expansion keeps empty arrays safe under set -u
  # on macOS's bash 3.2.
  if pandoc "$src" \
       ${REF_ARGS[@]+"${REF_ARGS[@]}"} \
       ${filter_args[@]+"${filter_args[@]}"} \
       -o "$OUTPUT/$name.docx" 2>"$OUTPUT/$name.log"; then
    echo "    -> $name.docx"
    [ -s "$OUTPUT/$name.log" ] || rm -f "$OUTPUT/$name.log"
  else
    echo "    !! DOCX failed (see $name.log)"
  fi

  # mermaid-filter drops an error file in the working directory;
  # remove it when empty, surface it when not.
  if [ -f "$SCRIPT_DIR/mermaid-filter.err" ]; then
    if [ -s "$SCRIPT_DIR/mermaid-filter.err" ]; then
      echo "    !! Mermaid rendering reported errors (see mermaid-filter.err)"
    else
      rm -f "$SCRIPT_DIR/mermaid-filter.err"
    fi
  fi

  # Move the original out of the inbox (timestamp avoids collisions)
  local stamp
  stamp="$(date '+%Y%m%d-%H%M%S')"
  mv "$src" "$PROCESSED/${name}-${stamp}.${base##*.}"
}

# --- Convert anything already sitting in the inbox at startup -------
shopt -s nullglob nocaseglob
for f in "$INBOX"/*.md "$INBOX"/*.markdown; do
  convert_file "$f"
done

# --- Watch loop ------------------------------------------------------
while true; do
  found=0
  for f in "$INBOX"/*.md "$INBOX"/*.markdown; do
    convert_file "$f"
    found=1
  done
  [ "$found" -eq 1 ] && echo "[$(date '+%H:%M:%S')] Waiting for more files..."
  sleep "$POLL_SECONDS"
done
