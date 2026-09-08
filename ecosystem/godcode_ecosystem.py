#!/usr/bin/env python3
"""
VOUDOO Ecosystem + PHB God Code Integration
Syncs token data with PHB system
"""

import json
import os

ECOSYSTEM_CONFIG = os.path.expanduser("~/phb-godcode-vortex/ecosystem/tokens.json")

def load_config():
    with open(ECOSYSTEM_CONFIG) as f:
        return json.load(f)

def get_ecosystem_status():
    config = load_config()
    tokens = config["tokens"]
    verified = sum(1 for t in tokens.values() if t.get("sourcify") == "exact_match")
    total = len(tokens)
    return {
        "verified": verified,
        "total": total,
        "percentage": (verified / total) * 100
    }

def sync_with_god_code():
    status = get_ecosystem_status()
    print(f"🔄 Syncing with PHB God Code...")
    print(f"   Verified: {status['verified']}/{status['total']}")
    print(f"   Percentage: {status['percentage']}%")
    
    # Save to PHB state
    state_file = os.path.expanduser("~/phb-godcode-vortex/ecosystem/state.json")
    with open(state_file, 'w') as f:
        json.dump(status, f, indent=2)
    
    print(f"✅ State saved to {state_file}")
    return status

if __name__ == "__main__":
    sync_with_god_code()
