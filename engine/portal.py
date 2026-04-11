PORTAL_MAP = {
    "LOW":   "VEIL-DOOR: THRESHOLD MIST",
    "MID":   "PORTAL: RESONANCE ARCH",
    "HIGH":  "GATE: VITRUVIAN SPHERE"
}

def portal_for_page(C, S):
    score = 0.5 * C + 0.5 * min(S, 1.0)
    if score < 0.7:
        return PORTAL_MAP["LOW"]
    elif score < 0.9:
        return PORTAL_MAP["MID"]
    else:
        return PORTAL_MAP["HIGH"]

def print_portal_layer(matches):
    print("PORTAL LAYER")
    print("------------")
    if not matches:
        print("No codex pages to map to portals.")
        print()
        return
    for i, (t, C, S, seq) in enumerate(matches, start=1):
        portal = portal_for_page(C, S)
        print(f"PAGE {i}: t={t:.1f}, C={C:.3f}, S={S:.3f} -> {portal}")
    print()
