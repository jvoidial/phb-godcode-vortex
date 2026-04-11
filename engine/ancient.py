from .codex import SYMBOL_MEANINGS

ANCIENT_CODEX_MAP = {
    "ENOCH": [
        "CIRCLE", "GRID", "RATIO", "LIGHT", "SHADOW"
    ],
    "KEBRA_NAGAST": [
        "CIRCLE", "SQUARE", "LINE", "RATIO", "LIGHT"
    ],
    "NESTORIAN_STELE": [
        "LIGHT", "RATIO", "GRID", "MIRROR", "CIRCLE"
    ],
    "MANICHAEAN": [
        "LIGHT", "SHADOW", "SPIRAL", "LINE", "MIRROR"
    ]
}

def print_ancient_codex():
    print("ANCIENT CODEX LAYER")
    print("-------------------")
    for name, seq in ANCIENT_CODEX_MAP.items():
        print(f"{name} SEQUENCE:")
        print("  " + " ".join(seq))
        print("  Symbolic reading:")
        for s in seq:
            meaning = SYMBOL_MEANINGS.get(s, "no mapping defined")
            print(f"    {s:8s} → {meaning}")
        print()
