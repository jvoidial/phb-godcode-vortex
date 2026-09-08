#!/bin/bash
# PHB Vortex Auto‑Service – runs HTTP server and tunnel, restarts on crash

cd ~/phb-godcode-vortex

# Start HTTP server (serves network_state.json)
while true; do
    echo "[$(date)] Starting HTTP server..."
    python3 -m http.server 8000 --bind 0.0.0.0
    echo "[$(date)] HTTP server stopped. Restarting in 5s..."
    sleep 5
done &
HTTP_PID=$!

# Start Cloudflare tunnel
while true; do
    echo "[$(date)] Starting Cloudflare tunnel..."
    cloudflared tunnel --url http://localhost:8000
    echo "[$(date)] Tunnel stopped. Restarting in 5s..."
    sleep 5
done &
TUNNEL_PID=$!

# Wait for them (they run forever)
wait
