#!/usr/bin/env bash
#
# eos-git-relocate.command  (added 2026-10-28, run once)
# -------------------------------------------------------------------
# Moves the git history from ~/.eos-git to <EOS folder>/.git.nosync.
# iCloud Drive skips anything whose name ends in .nosync, so the
# history still stays out of iCloud, and because it is inside the
# EOS folder, Claude's shell on this Mac can read git history again
# (it only sees connected folders). The .git pointer file is rewritten
# to a relative path so it resolves on the Mac and from Claude alike.
# Stop the EOS server first. Undo: reverse the mv and rewrite .git.
# -------------------------------------------------------------------
set -u
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EOS_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$EOS_ROOT" || exit 1
if lsof -nP -iTCP:"${EOS_PORT:-8765}" -sTCP:LISTEN >/dev/null 2>&1; then
  echo "The EOS server is running. Close its window, then run this again."; exit 1
fi
if [ -d "$EOS_ROOT/.git.nosync" ]; then
  echo "Already relocated: .git.nosync exists."
elif [ -d "$HOME/.eos-git" ]; then
  mv "$HOME/.eos-git" "$EOS_ROOT/.git.nosync" || exit 1
  printf 'gitdir: .git.nosync\n' > "$EOS_ROOT/.git"
  echo "Moved ~/.eos-git to .git.nosync inside the EOS folder."
else
  echo "Neither ~/.eos-git nor .git.nosync found; nothing to do."; exit 1
fi
echo "History intact: $(git rev-list --count HEAD) commits; remote: $(git remote get-url origin)"
echo "Done. Start the server again with eos-server.command."
