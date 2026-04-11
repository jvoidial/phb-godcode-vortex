import random
from .codex import SYMBOL_POOL, SYMBOL_MEANINGS

def evolve_deterministic(seq):
    evolved = seq[1:] + [seq[0]]
    if "GOLDEN" not in evolved:
        evolved[-1] = "GOLDEN"
    return evolved

def evolve_stochastic(seq, n=3):
    variants = []
    for _ in range(n):
        v = seq[:]
        for i in range(len(v)):
            if random.random() < 0.3:
                v[i] = random.choice(SYMBOL_POOL)
        variants.append(v)
    return variants

def evolve_hybrid(seq):
    base = evolve_deterministic(seq)
    variants = evolve_stochastic(base, n=2)
    return [base] + variants

def print_symbolic_meanings(seq):
    print("SYMBOLIC MEANINGS")
    print("-----------------")
    for s in seq:
        meaning = SYMBOL_MEANINGS.get(s, "no mapping defined")
        print(f"{s:8s} → {meaning}")
    print()

def print_evolution_block(seq, C, S):
    print("CODEX EVOLUTION")
    print("---------------")
    print(f"Base unlock coherence: {C:.6f}")
    print(f"Base unlock stability: {S:.6f}")
    print()

    det = evolve_deterministic(seq)
    print("Deterministic evolution:")
    print("  " + " ".join(det))
    print_symbolic_meanings(det)

    print("Stochastic evolution variants:")
    stoch = evolve_stochastic(seq, n=3)
    for i, v in enumerate(stoch, start=1):
        print(f"  Variant {i}: " + " ".join(v))
    print()

    print("Hybrid evolution set:")
    hyb = evolve_hybrid(seq)
    for i, v in enumerate(hyb, start=1):
        print(f"  Hybrid {i}: " + " ".join(v))
    print()
