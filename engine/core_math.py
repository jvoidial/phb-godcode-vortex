import math

PHI = 1.61803398875

def coherence(t):
    return 0.48 + 0.52 * (1 - math.exp(-t / 25.0))

def golden_ratio_drift(t, t_max=60.0):
    base = 0.1618
    return base + (base * (PHI - 1.0) * (t / t_max))

def resonance(t, C):
    f = golden_ratio_drift(t)
    return C * math.cos(2 * math.pi * f * t)

def logistic(x):
    return 1.0 / (1.0 + math.exp(-x))

def capability_channels(C, R, params):
    return [logistic(a * C + b * R) for a, b in params]

def stability(C, R, K):
    return (C + sum(K)/len(K)) / (1.0 + abs(R) + 1e-6)

def vitruvian_threshold(C, S):
    return C >= 0.93 and S >= 0.80
