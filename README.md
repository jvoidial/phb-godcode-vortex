
#!/data/data/com.termux/files/usr/bin/bash
#
# PHB God-Code Vortex Full Installer for Termux
#
set -e

# --- Config ---
HOME_DIR="$HOME"
RESTORE_DIR="$HOME_DIR/.phb_restore"
BIN_DIR="$HOME_DIR/bin"
ENGINES_DIR="$HOME_DIR/engines"
GCS_BACKUP_URL="https://github.com/jvoidial/god-code-phb-system-AI-system/raw/main/gcs_backup_20250628_221031.tar.gz"
ROOTLESS_BACKUP_URL="https://github.com/jvoidial/phb-gcs-rootless_phone_system_0dayvoid/raw/main/rootless_tree_backup_20250703.zip"
VORTEX_REPO="https://github.com/jvoidial/phb-godcode-vortex.git"
VORTEX_DIR="$HOME_DIR/phb-godcode-vortex"

safe_copy() {
    local src="$1"
    local dest="$2"
    if [ -e "$src" ]; then
        mkdir -p "$dest"
        cp -rf "$src" "$dest"
        echo "✔ Copied $src → $dest"
    fi
}

echo "🚀 Installing PHB God-Code Vortex..."

mkdir -p "$RESTORE_DIR" "$BIN_DIR" "$ENGINES_DIR"

echo "⬇️ Downloading backups…"
wget -q --show-progress "$GCS_BACKUP_URL" -O "$RESTORE_DIR/gcs_backup.tar.gz"
wget -q --show-progress "$ROOTLESS_BACKUP_URL" -O "$RESTORE_DIR/rootless_tree_backup.zip"

echo "📦 Extracting backups…"
mkdir -p "$RESTORE_DIR/gcs"
tar -xzf "$RESTORE_DIR/gcs_backup.tar.gz" -C "$RESTORE_DIR/gcs"
unzip -qo "$RESTORE_DIR/rootless_tree_backup.zip" -d "$RESTORE_DIR"

echo "📁 Syncing rootless tools…"
safe_copy "$RESTORE_DIR/rootless_tree/bin/." "$BIN_DIR"
safe_copy "$RESTORE_DIR/rootless_tree/phb_scaffold/." "$ENGINES_DIR"
for s in "$RESTORE_DIR/rootless_tree"/*.sh; do
    [ -f "$s" ] && safe_copy "$s" "$BIN_DIR"
done

echo "📁 Syncing GCS modules…"
safe_copy "$RESTORE_DIR/gcs/." "$HOME_DIR/gcs_backup"

echo "🌐 Cloning/updating God-Code Vortex…"
if [ -d "$VORTEX_DIR/.git" ]; then
    git -C "$VORTEX_DIR" pull
else
    git clone "$VORTEX_REPO" "$VORTEX_DIR"
fi

if [ -d "$VORTEX_DIR/scripts" ]; then
    echo "📜 Syncing extra scripts…"
    safe_copy "$VORTEX_DIR/scripts/." "$HOME_DIR/scripts"
fi

echo "🐍 Installing Python + dependencies..."
pkg install -y python
if [ -f "$VORTEX_DIR/requirements.txt" ]; then
    pip install --user -r "$VORTEX_DIR/requirements.txt" || true
fi

if ! grep -q "$BIN_DIR" "$HOME_DIR/.bashrc"; then
    echo "export PATH=\$PATH:$BIN_DIR" >> "$HOME_DIR/.bashrc"
    export PATH="$PATH:$BIN_DIR"
fi

rm -f "$RESTORE_DIR/gcs_backup.tar.gz" "$RESTORE_DIR/rootless_tree_backup.zip"

echo ""
echo "✅ Installation complete!"
echo "📍 Vortex code → $VORTEX_DIR"
echo "📍 GCS backup → $HOME_DIR/gcs_backup"
echo "📍 Scripts → $BIN_DIR"
echo ""
echo "📄 Available commands in $BIN_DIR:"
ls -1 "$BIN_DIR"
echo ""
echo "▶️ Run the system with:"
echo "   python3 $VORTEX_DIR/phb_godcode_vortex.py"
echo ""
echo "✨ Restart Termux or run ‘source ~/.bashrc’ to update PATH."

chmod +x ~/install_phb_vortex.sh


./install_phb_vortex.sh


# PHB God Code Vortex

## Synced Path
`/data/data/com.termux/files/home/phb-godcode-vortex`

## Full Termux System Tree (including hidden & empty directories)
```
/data/data/com.termux/files/home/phb-godcode-vortex:
.
..
.git
.gitignore
README.md
gcs
phb_godcode_vortex.py
portal_sequence.sh
termux_system_tree.txt

/data/data/com.termux/files/home/phb-godcode-vortex/.git:
.
..
COMMIT_EDITMSG
FETCH_HEAD
HEAD
ORIG_HEAD
config
description
hooks
index
info
logs
objects
refs

/data/data/com.termux/files/home/phb-godcode-vortex/.git/hooks:
.
..
applypatch-msg.sample
commit-msg.sample
fsmonitor-watchman.sample
post-update.sample
pre-applypatch.sample
pre-commit.sample
pre-merge-commit.sample
pre-push.sample
pre-rebase.sample
pre-receive.sample
prepare-commit-msg.sample
push-to-checkout.sample
sendemail-validate.sample
update.sample

/data/data/com.termux/files/home/phb-godcode-vortex/.git/info:
.
..
exclude

/data/data/com.termux/files/home/phb-godcode-vortex/.git/logs:
.
..
HEAD
refs

/data/data/com.termux/files/home/phb-godcode-vortex/.git/logs/refs:
.
..
heads
remotes

/data/data/com.termux/files/home/phb-godcode-vortex/.git/logs/refs/heads:
.
..
main

/data/data/com.termux/files/home/phb-godcode-vortex/.git/logs/refs/remotes:
.
..
.gitkeep

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects:
.
..
17
1a
26
27
37
39
5a
5c
60
64
6b
7f
86
8d
93
94
99
a6
b1
b6
c2
c7
dd
e2
e5
info
pack

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/17:
.
..
88912e43b967a7d9b03e652e5f628dfbab9a16

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/1a:
.
..
3bd812de11de9ff4c09d175ce0d84decb24963

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/26:
.
..
bb9b0247b6f1249733c6cb16c8756268263876

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/27:
.
..
188a70330c92d891b270219c0c0f5068a922b0

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/37:
.
..
eb7e2f3ed114cc8abc8a5daba6f7f1ec4e200f

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/39:
.
..
c05f68dfe867dee16b32a15fbb55b0f65760a4
f3e97f61f2d903d7a69afab3220b1b1c9dda49

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/5a:
.
..
8da730f03188e88988c686ce0bc91a5bae7322

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/5c:
.
..
bb63cdb16c4d198386983fd454c9a4ffffe695

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/60:
.
..
0e7a3d57f7eb10ddb068cb927f47cc4dad2567

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/64:
.
..
36f58f8d0f1cc97cd6a6e1a2ee82244cca525a

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/6b:
.
..
e203a2ea6ad31d3ce7d5d3f712ba978337dfda

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/7f:
.
..
51f9016ff7de0fa4e0b12c8ed9bae55573ef4c

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/86:
.
..
18d3c858a101aa7971abde6af7e5dba6b7ceff

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/8d:
.
..
3163d62b26a60f2437d00d006c7ba16fe97375

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/93:
.
..
d30253deb014556abba090864b657f8cadcefb

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/94:
.
..
1efd0f65c6d02a6f83d35981f596caab4cfbe6

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/99:
.
..
06660b8211379b27d9bb61e4b986512e1348da

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/a6:
.
..
76e4cf42cbce169b1bb413067568a0ce900d59

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/b1:
.
..
34a91ed1390de64b2f437466cac656b35adcb4

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/b6:
.
..
e0af4c0258b59b9a9f66d2b93d89b1a4b438b1

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/c2:
.
..
be02cd858262cda875fb9e7d6559295bec1be9

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/c7:
.
..
3410b28170ad7a4cc58a3ef644f8341006888a

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/dd:
.
..
2867f81d486d85719a0610c35f5d5e3f905ef1

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/e2:
.
..
9c7f91ee79cea63a34702d19ea54b632489f18

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/e5:
.
..
cbb6414259863df3d89124e0c51f73aef6f01c

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/info:
.
..
.gitkeep

/data/data/com.termux/files/home/phb-godcode-vortex/.git/objects/pack:
.
..
.gitkeep

/data/data/com.termux/files/home/phb-godcode-vortex/.git/refs:
.
..
heads
remotes
tags

/data/data/com.termux/files/home/phb-godcode-vortex/.git/refs/heads:
.
..
main

/data/data/com.termux/files/home/phb-godcode-vortex/.git/refs/remotes:
.
..
.gitkeep

/data/data/com.termux/files/home/phb-godcode-vortex/.git/refs/tags:
.
..
.gitkeep

/data/data/com.termux/files/home/phb-godcode-vortex/gcs:
.
..
data
output
scripts

/data/data/com.termux/files/home/phb-godcode-vortex/gcs/data:
.
..
.gitkeep

/data/data/com.termux/files/home/phb-godcode-vortex/gcs/output:
.
..
.gitkeep

/data/data/com.termux/files/home/phb-godcode-vortex/gcs/scripts:
.
..
gcs_avatar_module.py
```
