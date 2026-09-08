#!/usr/bin/env python3
"""
Auto‑generates multiple JSON feeds for different domains.
Runs every minute via cron.
"""

import json
import os
import random
import time
from datetime import datetime

DOMAINS = [
    "core",          # network_state_1.json
    "tokenomics",    # network_state_2.json
    "cosmic",        # network_state_3.json
    "consciousness", # network_state_4.json
]

def generate_page(domain, page_num):
    """Generate a single page with domain‑specific content."""
    # Base symbols
    base_symbols = ["CIRCLE", "SQUARE", "TRIANGLE", "RATIO", "LIGHT", "SHADOW", "MIRROR"]
    # Domain‑specific twists
    if domain == "tokenomics":
        symbols = ["BTC", "ETH", "USDC", "DAI", "UNI", "LINK", "AAVE"]
    elif domain == "cosmic":
        symbols = ["SIREN", "SERPO", "PROXIMA", "CENTAURI", "TRAPPIST", "KEPLER", "WOLF"]
    elif domain == "consciousness":
        symbols = ["SELF", "OTHER", "UNITY", "DUALITY", "AWARENESS", "DREAM", "REALITY"]
    else:
        symbols = base_symbols

    # Shuffle to create variation
    random.shuffle(symbols)

    # Generate voxels
    voxels = []
    for i, sym in enumerate(symbols[:5]):  # use first 5
        voxels.append({
            "x": i,
            "y": 0,
            "z": i,
            "symbol": sym,
            "meaning": f"{sym} meaning for {domain}"
        })

    return {
        "page": page_num,
        "time": random.randint(1, 10),
        "coherence": round(random.uniform(0.5, 1.0), 6),
        "stability": round(random.uniform(0.5, 1.2), 6),
        "resonance": round(random.uniform(0.1, 0.5), 6),
        "sequence": symbols,
        "portal": f"PORTAL: {domain.upper()}",
        "voxels": voxels,
        "veil": {
            "thickness": round(random.uniform(0.1, 0.8), 6),
            "phase": random.choice(["THIN", "SEALED", "TURBULENT", "CLEAR"]),
            "breach_probability": round(random.uniform(0.2, 0.9), 6),
            "narrative": f"The {domain} veil is shifting: {random.choice(['states merge', 'patterns emerge', 'boundaries dissolve'])}."
        },
        "energy": {
            "magnitude": round(random.uniform(0.5, 1.5), 6),
            "band": random.choice(["LOW", "MID", "HIGH"]),
            "color": random.choice(["LIGHT", "DARK", "NEUTRAL"])
        }
    }

def generate_feed(domain, index):
    """Generate a complete JSON feed for a domain."""
    # Number of pages grows over time (simulate evolution)
    base_pages = 1
    # Use timestamp to determine how many pages (each minute adds a chance for a new page)
    # For demo, we'll generate 2 pages for cosmic, 3 for core, etc.
    if domain == "core":
        num_pages = 2
    elif domain == "cosmic":
        num_pages = 3
    else:
        num_pages = 2

    pages = [generate_page(domain, i+1) for i in range(num_pages)]

    feed = {
        "timestamp": datetime.now().strftime("%a %b %d %H:%M:%S %Y"),
        "domain": domain,
        "pages": pages,
        "vitruvian_state": [num_pages, 0.9, 0.8],  # placeholder
    }
    # Add some top‑level fields for easy access
    feed["coherence"] = pages[-1]["coherence"]
    feed["stability"] = pages[-1]["stability"]
    feed["energy"] = pages[-1]["energy"]["magnitude"]
    feed["veil"] = pages[-1]["veil"]["phase"]
    feed["portal"] = 1.0 if pages[-1]["portal"] else 0

    return feed

def main():
    for i, domain in enumerate(DOMAINS, start=1):
        feed = generate_feed(domain, i)
        filename = f"gcs/network_state_{i}.json"
        with open(filename, 'w') as f:
            json.dump(feed, f, indent=2)
        print(f"✅ Generated {filename}")

if __name__ == "__main__":
    main()
