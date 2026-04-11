#!/data/data/com.termux/files/usr/bin/sh
set -e
pkg install -y python > /dev/null 2>&1 || true
python3 phb_godcode_vortex.py | tee phb_godcode_vortex_log.txt
