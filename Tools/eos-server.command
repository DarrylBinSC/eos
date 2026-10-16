#!/usr/bin/env bash
#
# eos-server.command
# -------------------------------------------------------------------
# Starts the EOS Registers web app (Tools/eos_server.py) for this Mac
# and the home network. Double-click in Finder, or run from Terminal.
# Press Ctrl-C (or close the window) to stop it.
#
# Settings (edit here):
#   EOS_PORT      port to listen on (default 8765)
#   EOS_BIND      0.0.0.0 = reachable from other devices on the LAN;
#                 127.0.0.1 = this Mac only
#   EOS_PASSWORD  leave empty for no login (Darryl, 2026-10-15). Set a
#                 value to require a password in the browser.
# -------------------------------------------------------------------
set -u
export EOS_PORT="${EOS_PORT:-8765}"
export EOS_BIND="${EOS_BIND:-0.0.0.0}"
export EOS_PASSWORD="${EOS_PASSWORD:-}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EOS_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
export EOS_ROOT
cd "$EOS_ROOT" || exit 1

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 not found. Install the Xcode command line tools (xcode-select --install) or Homebrew python, then re-run."
  exit 1
fi

# --- git: the register history. First run initializes the repo on this Mac. ---
if ! command -v git >/dev/null 2>&1; then
  echo "git not found. Install the Xcode command line tools (xcode-select --install), then re-run."
  exit 1
fi
# Track text only. The EOS folder is iCloud-synced and holds hundreds of cloud-only Word,
# PowerPoint and PDF files; adding those to git forces every one to download (the first run
# hung on exactly that, 2026-10-15). The history is for the registers and markdown anyway.
cat > "$EOS_ROOT/.gitignore" <<'EOG'
.DS_Store
**/.DS_Store
~$*
*.docx
*.dotx
*.pptx
*.xlsx
*.pdf
*.png
*.jpg
*.jpeg
*.gif
*.svg
*.zip
*.log
*.diff
__pycache__/
*.pyc
Pandoc/output/
Pandoc/processed/
Pandoc/samples/
Pandoc/miro_exports/
Pandoc/inbox/
Dashboard/
Claude outputs/
EOG

if [ ! -d "$EOS_ROOT/.git" ] || ! git -C "$EOS_ROOT" rev-parse HEAD >/dev/null 2>&1; then
  echo "Initializing git history for the EOS folder (text files only)..."
  [ -d "$EOS_ROOT/.git" ] || git init -q "$EOS_ROOT"
  rm -f "$EOS_ROOT/.git/index.lock"
  git -C "$EOS_ROOT" config user.name "Darryl Benson"
  git -C "$EOS_ROOT" config user.email "dsben@sbcglobal.net"
  git -C "$EOS_ROOT" add -A
  git -C "$EOS_ROOT" commit -q -m "EOS: initial commit after the 2026-10-15 move to one item per file (Registers/)"
  echo "Done: $(git -C "$EOS_ROOT" ls-files | wc -l | tr -d ' ') text files tracked."
fi

LAN_IP="$(ipconfig getifaddr en0 2>/dev/null || ipconfig getifaddr en1 2>/dev/null || echo '<this-mac-ip>')"
echo "EOS root: $EOS_ROOT"
echo "On this Mac:        http://localhost:$EOS_PORT"
echo "From other devices: http://$LAN_IP:$EOS_PORT   (also try http://$(hostname -s).local:$EOS_PORT)"
echo
exec python3 "$SCRIPT_DIR/eos_server.py"
