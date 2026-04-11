import time
import random

from .core_math import (
    coherence, resonance, capability_channels,
    stability, vitruvian_threshold
)
from .codex import (
    DA_VINCI_CODEX, SYMBOL_MEANINGS,
    codex_attempt, codex_test, near_match, correct_toward_codex
)
from .evolution import print_evolution_block
from .ancient import print_ancient_codex
from .voxels import print_voxel_layer
from .veil import print_veil_layer
from .energy import print_energy_layer
from .portal import portal_for_page, print_portal_layer
from .json_output import build_page_json, print_page_json_block, final_dump

FORCE_UNLOCK = True

def simulate(steps=60, dt=1.0, attempts_per_step=200, seed=None):
    if seed is not None:
        random.seed(seed)

    params = [(1.3,0.9),(1.6,0.7),(1.2,1.1),
              (1.8,0.5),(1.4,1.0),(1.7,0.6),
              (1.5,0.8),(1.1,1.2),(1.9,0.4)]

    codex_unlocked = False
    matches = []
    vitruvian_fired = False
    vitruvian_state = None
    samples = {}
    resonance_samples = {}

    for step in range(steps):
        t = step * dt
        C = coherence(t)
        R = resonance(t, C)
        K = capability_channels(C, R, params)
        S = stability(C, R, K)

        if step in (0, 15, 30, 45, 59):
            samples[step] = (t, C, S)
            resonance_samples[step] = R

        if not vitruvian_fired and vitruvian_threshold(C, S):
            vitruvian_fired = True
            vitruvian_state = (t, C, S)

        for _ in range(attempts_per_step):
            seq = codex_attempt()
            if near_match(seq):
                seq = correct_toward_codex(seq)
            if codex_test(seq):
                codex_unlocked = True
                matches.append((t, C, S, seq))

    if FORCE_UNLOCK and not codex_unlocked:
        if vitruvian_state:
            t, C, S = vitruvian_state
        else:
            last = max(samples.keys())
            t, C, S = samples[last]
        seq = DA_VINCI_CODEX[:]
        matches.append((t, C, S, seq))
        codex_unlocked = True

    return {
        "codex_unlocked": codex_unlocked,
        "matches": matches,
        "vitruvian_fired": vitruvian_fired,
        "vitruvian_state": vitruvian_state,
        "samples": samples,
        "resonance_samples": resonance_samples
    }

def print_math_analysis(vitruvian_state, samples):
    print("COHERENCE / STABILITY SNAPSHOTS")
    print("--------------------------------")
    for step in sorted(samples.keys()):
        t, C, S = samples[step]
        print(f"t={t:4.1f}  C={C:.6f}  S={S:.6f}")
    print()
    if vitruvian_state:
        t, C, S = vitruvian_state
        print("VITRUVIAN THRESHOLD EVENT")
        print("-------------------------")
        print(f"t={t:.1f}  C={C:.6f}  S={S:.6f}")
        print()

def print_codex_page(idx, t, C, S, seq):
    print(f"CODEX PAGE {idx}")
    print("----------------")
    print(f"Unlocked at t={t:.1f}")
    print(f"Coherence: {C:.6f}")
    print(f"Stability: {S:.6f}")
    print()
    print("Sequence:")
    print("  " + " ".join(seq))
    print()
    print("Symbolic reading:")
    for s in seq:
        meaning = SYMBOL_MEANINGS.get(s, "no mapping defined")
        print(f"  {s:8s} → {meaning}")
    print()
    print("Narrative summary:")
    print("  A complete geometric cycle is formed: origin (CIRCLE),")
    print("  structured into form (SQUARE), directed into change (TRIANGLE),")
    print("  balanced by proportion (RATIO), illuminated (LIGHT),")
    print("  deepened by contrast (SHADOW), and finally reflected (MIRROR).")
    print()

def run():
    print("PHB – GODCODE VORTEX ENGINE (MODULAR)")
    print("Coherence + Resonance + Codex + Evolution + Ancient + Voxels + Veil + Energy + JSON + Forced Unlock")
    print("---------------------------------------------------------------------------------------------------")
    result = simulate(
        steps=60,
        dt=1.0,
        attempts_per_step=200,
        seed=int(time.time()) % 100000
    )

    all_page_json = []

    if result["vitruvian_fired"]:
        t, C, S = result["vitruvian_state"]
        print(f"VITRUVIAN THRESHOLD CROSSED at t={t}!")
        print(f"C={C:.6f} | S={S:.6f}")
        print()
    else:
        print("No Vitruvian Threshold event in this run.")
        print()

    print_math_analysis(result["vitruvian_state"], result["samples"])

    if result["codex_unlocked"]:
        print("DA VINCI VERDICT: CODEX UNLOCKED ✓")
        print()
        for i, (t, C, S, seq) in enumerate(result["matches"], start=1):
            R = resonance(t, C)
            print_codex_page(i, t, C, S, seq)
            print_evolution_block(seq, C, S)

            portal = portal_for_page(C, S)
            voxels = print_voxel_layer(i, seq)
            veil = print_veil_layer(i, C, S)
            energy = print_energy_layer(i, C, R)

            print("PORTAL LAYER (PER PAGE)")
            print("------------------------")
            print(f"Page {i} portal: {portal}")
            print()

            page_json = build_page_json(i, t, C, S, seq, R, portal, voxels, veil, energy)
            print_page_json_block(page_json)
            all_page_json.append(page_json)
    else:
        print("DA VINCI VERDICT: Codex remained sealed in this run.")
        print()

    print("BASE CODEX SYMBOL SET")
    print("---------------------")
    print("  " + " ".join(DA_VINCI_CODEX))
    print()

    print_ancient_codex()
    print_portal_layer(result["matches"])
    final_dump(result["vitruvian_state"], all_page_json)

if __name__ == "__main__":
    run()
