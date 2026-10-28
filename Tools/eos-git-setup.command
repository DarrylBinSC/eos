#!/usr/bin/env bash
#
# eos-git-setup.command  (added 2026-10-28)
# -------------------------------------------------------------------
# One-time setup, run on the Mac that hosts the EOS server. Does two
# things, each reversible:
#
#   1. Moves the git history (.git, ~120 MB of fast-changing objects)
#      out of the iCloud-synced EOS folder to ~/.eos-git, and leaves a
#      one-line ".git" file behind that points to it. git supports this
#      natively; the server and every git command keep working. iCloud
#      then syncs the working files only.
#      Undo: delete the .git file and move ~/.eos-git back to .git.
#
#   2. Adds a private GitHub repository as the backup remote ("origin")
#      and makes the first push. The server pushes after every commit
#      from then on. You are asked for the repository URL, then for
#      your GitHub username and a personal access token (used as the
#      password; macOS Keychain remembers it).
#      Undo: git remote remove origin
#
# Stop the EOS server first (close its Terminal window). The script
# refuses to run while it is up.
# -------------------------------------------------------------------
set -u
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EOS_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
GIT_HOME="$EOS_ROOT/.git.nosync"   # was ~/.eos-git on first run; relocated 2026-10-28 so Claude's shell can read it
cd "$EOS_ROOT" || exit 1

if lsof -nP -iTCP:"${EOS_PORT:-8765}" -sTCP:LISTEN >/dev/null 2>&1; then
  echo "The EOS server is running on port ${EOS_PORT:-8765}. Close its window, then run this again."
  exit 1
fi
if ! git rev-parse HEAD >/dev/null 2>&1; then
  echo "No git history found in $EOS_ROOT. Run eos-server.command once first."
  exit 1
fi

echo "== Step 1: move the git history out of iCloud"
if [ -d "$EOS_ROOT/.git" ]; then
  if [ -e "$GIT_HOME" ]; then
    echo "$GIT_HOME already exists; not overwriting it. Resolve that first."
    exit 1
  fi
  mv "$EOS_ROOT/.git" "$GIT_HOME" || exit 1
  printf 'gitdir: .git.nosync\n' > "$EOS_ROOT/.git"
  echo "Moved to $GIT_HOME; .git in the EOS folder is now a pointer file."
elif [ -f "$EOS_ROOT/.git" ]; then
  echo "Already a pointer file: $(cat "$EOS_ROOT/.git")"
fi
git status --short >/dev/null || { echo "git cannot read the repository after the move; stopping."; exit 1; }
echo "History intact: $(git rev-list --count HEAD) commits."
echo

echo "== Step 2: GitHub backup remote"
git config credential.helper osxkeychain
if git remote get-url origin >/dev/null 2>&1; then
  echo "Remote already set: $(git remote get-url origin)"
else
  echo "Paste the repository URL from GitHub (green Code button, HTTPS tab),"
  echo "it looks like https://github.com/<your-username>/<repo>.git"
  read -r -p "URL: " URL
  case "$URL" in
    https://github.com/*) ;;
    *) echo "That does not look like a GitHub HTTPS URL. Nothing changed."; exit 1 ;;
  esac
  git remote add origin "$URL"
fi
echo "Pushing the history to GitHub. When asked:"
echo "  Username: your GitHub username"
echo "  Password: the personal access token (not your GitHub password)"
if git push -u origin main; then
  echo
  echo "Done. GitHub now holds a copy of the history, and the server will push after every commit."
else
  echo
  echo "Push failed. The remote is set; fix the credentials and run: git push -u origin main"
  exit 1
fi
