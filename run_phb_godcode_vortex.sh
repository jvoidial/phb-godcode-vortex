#!/data/data/com.termux/files/usr/bin/sh
set -e

# Always run from the script's directory
cd "$(dirname "$0")"

echo "PHB Smart Mode Launcher"
echo "------------------------"

# Prefer modular engine if present
if [ -d "engine" ]; then
    echo "→ Modular engine detected. Running: python3 -m engine"
    pkg install -y python > /dev/null 2>&1 || true
    python3 -m engine | tee phb_godcode_vortex_log.txt
    exit 0
fi

# Fallback to single-file engine
if [ -f "phb_godcode_vortex.py" ]; then
    echo "→ Single-file engine detected. Running: python3 phb_godcode_vortex.py"
    pkg install -y python > /dev/null 2>&1 || true
    python3 phb_godcode_vortex.py | tee phb_godcode_vortex_log.txt
    exit 0
fi

# If neither exists
echo "✗ ERROR: No engine found."
echo "Expected either:"
echo "  • engine/ directory"
echo "  • phb_godcode_vortex.py"
exit 1
