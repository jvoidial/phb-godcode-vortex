#!/data/data/com.termux/files/usr/bin/sh
set -e

cd "$(dirname "$0")/.."

echo "PHB + P2P ORCHESTRATOR"
echo "-----------------------"

# 1) Run PHB engine
if [ -x "./run_phb_godcode_vortex.sh" ]; then
    echo "→ Running PHB Smart Mode engine..."
    ./run_phb_godcode_vortex.sh
fi

echo
echo "P2P LAYER"
echo "---------"

# 2) Start listener
if [ -f "gcs/scripts/p2p_listener.py" ]; then
    echo "→ Starting P2P listener (background)..."
    nohup python3 gcs/scripts/p2p_listener.py > gcs/p2p_listener.log 2>&1 &
fi

# 3) Auto-broadcast FINAL JSON DUMP
if [ -f "gcs/phb_auto_broadcast.py" ] && [ -f "gcs/scripts/p2p_send_auto.py" ]; then
    if [ -f "phb_godcode_vortex_log.txt" ]; then
        echo "→ Auto-broadcasting FINAL JSON DUMP to peers..."
        python3 gcs/phb_auto_broadcast.py | python3 gcs/scripts/p2p_send_auto.py
    else
        echo "✗ No PHB log found; nothing to broadcast"
    fi
fi

echo
echo "PHB + P2P orchestration complete."
