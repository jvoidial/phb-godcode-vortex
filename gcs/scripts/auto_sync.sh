#!/data/data/com.termux/files/usr/bin/bash

cd ~/phb-godcode-vortex || exit 0

# Run documentation updater
bash gcs/scripts/update_docs.sh >/dev/null 2>&1

# Stage changes silently
git add README.md installer.sh >/dev/null 2>&1

# Only commit if there are changes
if ! git diff --cached --quiet; then
    git commit -m "Auto-sync: updated README + installer" >/dev/null 2>&1
    git push >/dev/null 2>&1
    echo "[PHB] Auto-sync: pushed updated docs."
else
    echo "[PHB] Auto-sync: no changes."
fi
