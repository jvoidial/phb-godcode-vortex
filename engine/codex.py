import random

DA_VINCI_CODEX = [
    "CIRCLE", "SQUARE", "TRIANGLE",
    "RATIO", "LIGHT", "SHADOW", "MIRROR"
]

SYMBOL_POOL = [
    "CIRCLE", "SQUARE", "TRIANGLE", "RATIO",
    "LIGHT", "SHADOW", "MIRROR",
    "SPIRAL", "ARC", "POINT", "LINE",
    "VESICA", "GOLDEN", "GRID"
]

SYMBOL_MEANINGS = {
    "CIRCLE":  "origin, cycles, unity",
    "SQUARE":  "structure, boundaries, grounding",
    "TRIANGLE":"transformation, direction, change",
    "RATIO":   "proportion, balance, measure",
    "LIGHT":   "clarity, insight, revelation",
    "SHADOW":  "contrast, depth, hidden aspects",
    "MIRROR":  "reflection, self-awareness, feedback",
    "SPIRAL":  "growth, unfolding, iteration",
    "ARC":     "partial view, transition",
    "POINT":   "focus, singularity",
    "LINE":    "connection, path, vector",
    "VESICA":  "overlap, intersection, shared space",
    "GOLDEN":  "harmonic proportion, elegance",
    "GRID":    "system, lattice, framework"
}

def insight_biased_choice():
    weights = {
        "CIRCLE": 20, "SQUARE": 20, "TRIANGLE": 20,
        "RATIO": 15, "LIGHT": 10, "SHADOW": 10, "MIRROR": 10,
        "SPIRAL": 1, "ARC": 1, "POINT": 1, "LINE": 1,
        "VESICA": 1, "GOLDEN": 1, "GRID": 1
    }
    symbols = list(weights.keys())
    probs = [weights[s] for s in symbols]
    return random.choices(symbols, probs)[0]

def codex_attempt():
    return [insight_biased_choice() for _ in range(len(DA_VINCI_CODEX))]

def codex_test(seq):
    return seq == DA_VINCI_CODEX

def near_match(seq):
    score = sum(1 for a, b in zip(seq, DA_VINCI_CODEX) if a == b)
    return score >= 5

def correct_toward_codex(seq):
    return [
        DA_VINCI_CODEX[i] if random.random() < 0.5 else seq[i]
        for i in range(len(seq))
    ]
