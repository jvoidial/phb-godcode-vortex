def veil_state(C, S):
    thickness = max(0.0, 1.0 - 0.5*(C + min(S,1.0)))
    if thickness > 0.7:
        phase = "OPAQUE"
        narrative = "The veil is dense; only echoes pass through."
    elif thickness > 0.3:
        phase = "TRANSLUCENT"
        narrative = "The veil shimmers; forms are sensed but not fully seen."
    else:
        phase = "THIN"
        narrative = "The veil is almost gone; states bleed into each other."
    breach_prob = max(0.0, 1.0 - thickness)
    return {
        "thickness": thickness,
        "phase": phase,
        "breach_probability": breach_prob,
        "narrative": narrative
    }

def print_veil_layer(page_index, C, S):
    print("VEIL SIMULATOR LAYER")
    print("--------------------")
    vs = veil_state(C, S)
    print(f"Page {page_index} veil state:")
    print(f"  thickness: {vs['thickness']:.3f}")
    print(f"  phase: {vs['phase']}")
    print(f"  breach_probability: {vs['breach_probability']:.3f}")
    print(f"  narrative: {vs['narrative']}")
    print()
    return vs
