import json
import time

def build_page_json(page_index, t, C, S, seq, R, portal, voxels, veil, energy):
    return {
        "page": page_index,
        "time": t,
        "coherence": C,
        "stability": S,
        "resonance": R,
        "sequence": seq,
        "portal": portal,
        "voxels": voxels,
        "veil": veil,
        "energy": energy
    }

def print_page_json_block(page_json):
    print("JSON BLOCK")
    print("----------")
    print(json.dumps(page_json, indent=2))
    print()

def final_dump(vitruvian_state, pages):
    print("FINAL JSON DUMP")
    print("---------------")
    print(json.dumps({
        "timestamp": time.ctime(),
        "vitruvian_state": vitruvian_state,
        "pages": pages
    }, indent=2))
    print()
