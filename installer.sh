#!/data/data/com.termux/files/usr/bin/bash
echo "[PHB] Initialising installer..."

pkg update -y >/dev/null 2>&1
pkg upgrade -y >/dev/null 2>&1
pkg install python git -y >/dev/null 2>&1

echo "[PHB] Syncing repository..."
if [ -d "$HOME/phb-godcode-vortex/.git" ]; then
    cd ~/phb-godcode-vortex
    git pull -q
else
    git clone -q https://github.com/jvoidial/phb-godcode-vortex.git ~/phb-godcode-vortex
    cd ~/phb-godcode-vortex
fi

mkdir -p gcs gcs/data gcs/output gcs/scripts

[ ! -f "gcs/network_state.json" ] && echo "{}" > gcs/network_state.json

chmod +x run_phb_godcode_vortex.sh 2>/dev/null
chmod +x gcs/run_phb_p2p.sh 2>/dev/null
chmod +x gcs/scripts/*.py 2>/dev/null
chmod +x gcs/scripts/*.sh 2>/dev/null

echo "[PHB] Installation complete."
echo "[PHB] Launch with: ./gcs/run_phb_p2p.sh"
