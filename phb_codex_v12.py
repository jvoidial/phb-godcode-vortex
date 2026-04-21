import math
import random
import copy

# -----------------------------
# PHB CODEX v12 – FULL SCRIPT
# -----------------------------

# --- PARAMETERS ---
PHI = 1.61803398875
f_base = 0.1618

DA_VINCI_CODEX = ["CIRCLE", "SQUARE", "TRIANGLE", "RATIO", "LIGHT", "SHADOW", "MIRROR"]

SYMBOL_POOL = ["CIRCLE", "SQUARE", "TRIANGLE", "RATIO", "LIGHT", "SHADOW", "MIRROR",
               "SPIRAL", "ARC", "POINT", "LINE", "VESICA", "GOLDEN", "GRID"]

SYMBOL_WEIGHTS = {
    "CIRCLE": 20, "SQUARE": 20, "TRIANGLE": 20,
    "RATIO": 15, "LIGHT": 10, "SHADOW": 10, "MIRROR": 10,
    "SPIRAL": 1, "ARC": 1, "POINT": 1, "LINE": 1, "VESICA": 1, "GOLDEN": 1, "GRID": 1
}

SYMBOL_MEANINGS = {
    "CIRCLE": "origin, cycles, unity",
    "SQUARE": "structure, boundaries, grounding",
    "TRIANGLE": "transformation, direction, change",
    "RATIO": "proportion, balance, measure",
    "LIGHT": "clarity, insight, revelation",
    "SHADOW": "contrast, depth, hidden aspects",
    "MIRROR": "reflection, self-awareness, feedback",
    "SPIRAL": "growth, unfolding, iteration",
    "ARC": "partial view, transition",
    "POINT": "focus, singularity",
    "LINE": "connection, path, vector",
    "VESICA": "overlap, intersection, shared space",
    "GOLDEN": "harmonic proportion, elegance",
    "GRID": "system, lattice, framework"
}

# Logistic parameters for capability channels
CHANNEL_PARAMS = [(1.5, 0.5), (1.2, 0.7), (1.0, 1.0)]

# -----------------------------
# CORE FUNCTIONS
# -----------------------------

def coherence(t):
    return 0.48 + 0.52 * (1 - math.exp(-t / 25))

def golden_drift(t, t_max):
    return f_base + f_base * (PHI - 1) * (t / t_max)

def resonance(C, t, t_max):
    f = golden_drift(t, t_max)
    return C * math.cos(2 * math.pi * f * t)

def capability_channels(C, R):
    return [1 / (1 + math.exp(-(a * C + b * R))) for a, b in CHANNEL_PARAMS]

def stability(C, K, R):
    avg_K = sum(K)/len(K)
    return (C + avg_K) / (1 + abs(R))

def vitruvian_threshold(C, S):
    return C >= 0.93 and S >= 0.80

# --- SYMBOLIC FUNCTIONS ---

def weighted_choice(pool, weights):
    w = [weights.get(sym, 1) for sym in pool]
    return random.choices(pool, weights=w, k=1)[0]

def codex_attempt():
    return [weighted_choice(SYMBOL_POOL, SYMBOL_WEIGHTS) for _ in DA_VINCI_CODEX]

def codex_test(seq):
    return seq == DA_VINCI_CODEX

def near_match(seq):
    return sum([s1==s2 for s1,s2 in zip(seq, DA_VINCI_CODEX)]) >= 5

def correct_toward_codex(seq):
    corrected = seq[:]
    for i in range(len(seq)):
        if corrected[i] != DA_VINCI_CODEX[i] and random.random() < 0.5:
            corrected[i] = DA_VINCI_CODEX[i]
    return corrected

# -----------------------------
# SIMULATION LOOP
# -----------------------------

def simulate(steps=60, dt=1.0, attempts_per_step=200, seed=None):
    if seed is not None:
        random.seed(seed)
    matches = []
    vitruvian_fired = False
    vitruvian_state = None
    samples = []

    for step in range(steps):
        t = step * dt
        C = coherence(t)
        R = resonance(C, t, steps*dt)
        K = capability_channels(C, R)
        S = stability(C, K, R)

        if step % (steps//4) == 0:
            samples.append((t, C, S))

        if not vitruvian_fired and vitruvian_threshold(C, S):
            vitruvian_fired = True
            vitruvian_state = (t, C, S)

        for _ in range(attempts_per_step):
            seq = codex_attempt()
            if near_match(seq):
                seq = correct_toward_codex(seq)
            if codex_test(seq):
                matches.append((t, C, S, seq))
                break

    return len(matches) > 0, matches, vitruvian_fired, vitruvian_state, samples

# -----------------------------
# EVOLUTION FUNCTIONS
# -----------------------------

def evolve_deterministic(seq):
    seq_det = seq[1:] + [seq[0]]
    seq_det[-1] = "GOLDEN"
    return seq_det

def evolve_stochastic(seq, variants=3, p=0.3):
    variant_list = []
    for _ in range(variants):
        v = [random.choice(SYMBOL_POOL) if random.random()<p else s for s in seq]
        variant_list.append(v)
    return variant_list

def evolve_hybrid(seq):
    return evolve_stochastic(evolve_deterministic(seq), variants=3, p=0.2)

def symbolic_reading(seq):
    return [f"{s} → {SYMBOL_MEANINGS.get(s,'unknown')}" for s in seq]

# -----------------------------
# PRINT FUNCTIONS
# -----------------------------

def print_codex_page(t,C,S,seq):
    print(f"\n--- CODEX PAGE ---")
    print(f"Unlock time: {t}")
    print(f"Coherence: {C:.3f}")
    print(f"Stability: {S:.3f}")
    print(f"Sequence: {seq}")
    print("Symbolic reading:")
    for line in symbolic_reading(seq):
        print("  ", line)
    print("Narrative:")
    print("  A complete geometric cycle is formed: "+", ".join(seq)+".")

def print_evolution_block(seq,C,S):
    print("\n--- CODEX EVOLUTION ---")
    print(f"Base unlock coherence: {C:.3f}, stability: {S:.3f}")
    print("\nDeterministic Evolution:")
    for line in symbolic_reading(evolve_deterministic(seq)):
        print("  ", line)
    print("\nStochastic Variants:")
    for v in evolve_stochastic(seq):
        print("  ", v)
    print("\nHybrid Variants:")
    for v in evolve_hybrid(seq):
        print("  ", v)

def print_base_codex():
    print("\n--- BASE CODEX SYMBOL SET ---")
    for s in DA_VINCI_CODEX:
        print(f"  {s} → {SYMBOL_MEANINGS[s]}")

# -----------------------------
# MAIN EXECUTION
# -----------------------------

def main():
    codex_unlocked, matches, vitruvian_fired, vitruvian_state, samples = simulate()

    print("\n=== PHB CODEX SIMULATION v12 ===")
    if vitruvian_fired:
        t, C, S = vitruvian_state
        print(f"Vitruvian Threshold crossed at t={t}, C={C:.3f}, S={S:.3f}")
    else:
        print("Vitruvian Threshold not reached.")

    print("\nCoherence/Stability snapshots:")
    for t, C, S in samples:
        print(f"  t={t}, C={C:.3f}, S={S:.3f}")

    if codex_unlocked:
        for t, C, S, seq in matches:
            print_codex_page(t,C,S,seq)
            print_evolution_block(seq,C,S)
    else:
        print("Codex remained sealed.")

    print_base_codex()

if __name__ == "__main__":
    main()
