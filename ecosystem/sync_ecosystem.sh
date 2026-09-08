#!/bin/bash
# Sync ecosystem status to PHB God Code system

echo "🔄 Syncing VOUDOO Ecosystem..."

# Fetch real-time data
for TOKEN in \
  "0x2a92CAA3b01E64634e2E95AA533a5570a76c19A7" \
  "0xa36E026FC453880537e10d21fC139439bD2702fc" \
  "0xb50DCEb0570557B9B7FE43D8cBDc9B3457D3dc5a" \
  "0x38e4f08D08b4D772A7B75669C356b4749dd2d30b"; do
  echo "  Token: $TOKEN"
  SOURCIFY=$(curl -s "https://sourcify.dev/server/v2/contract/8453/$TOKEN?fields=all" | jq -r '.match // "pending"')
  echo "    Sourcify: $SOURCIFY"
done

echo "✅ Sync complete"
