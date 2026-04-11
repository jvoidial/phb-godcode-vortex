def energy_signature(C, R):
    magnitude = abs(C * (1.0 + R))
    if magnitude < 0.5:
        band = "LOW"
        color = "SHADOW"
    elif magnitude < 1.0:
        band = "MID"
        color = "LIGHT"
    else:
        band = "HIGH"
        color = "GOLDEN"
    return {
        "magnitude": magnitude,
        "band": band,
        "color": color
    }

def print_energy_layer(page_index, C, R):
    print("ENERGY LAYER")
    print("------------")
    es = energy_signature(C, R)
    print(f"Page {page_index} energy:")
    print(f"  magnitude: {es['magnitude']:.3f}")
    print(f"  band: {es['band']}")
    print(f"  color: {es['color']}")
    print()
    return es
