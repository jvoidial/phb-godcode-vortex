#!/bin/bash
# Launcher for the PHB CORS server – keeps it running forever

cd ~/phb-godcode-vortex

while true; do
    echo "🔄 Starting PHB CORS server (secure) at $(date)"
    python3 serve_cors_secure.py
    echo "⚠️ Server stopped. Restarting in 5 seconds..."
    sleep 5
done
