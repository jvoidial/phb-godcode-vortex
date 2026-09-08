#!/bin/bash
# Update phb_url.json in the repository with current tunnel URL

cd ~/phb-godcode-vortex
TUNNEL_URL=$(grep -o 'https://[a-zA-Z0-9.-]*\.trycloudflare\.com' cloudflared.log | tail -1)
if [ -n "$TUNNEL_URL" ]; then
    cd ~/spirit-guide-token
    echo "{\"url\": \"$TUNNEL_URL/gcs/network_state.json\"}" > phb_url.json
    git add phb_url.json
    git commit -m "🔄 Update PHB tunnel URL" 2>/dev/null
    git push -f
    echo "[$(date)] Updated PHB URL: $TUNNEL_URL"
else
    echo "[$(date)] No tunnel URL yet."
fi
