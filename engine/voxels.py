from .codex import SYMBOL_MEANINGS

def build_voxels_for_sequence(seq):
    voxels = []
    for i, symbol in enumerate(seq):
        voxel = {
            "x": i,
            "y": 0,
            "z": i,
            "symbol": symbol,
            "meaning": SYMBOL_MEANINGS.get(symbol, "no mapping defined")
        }
        voxels.append(voxel)
    return voxels

def print_voxel_layer(page_index, seq):
    print("VOXEL LAYER")
    print("-----------")
    voxels = build_voxels_for_sequence(seq)
    print(f"Page {page_index} voxel grid:")
    for v in voxels:
        print(f"  ({v['x']},{v['y']},{v['z']}) -> {v['symbol']} : {v['meaning']}")
    print()
    return voxels
