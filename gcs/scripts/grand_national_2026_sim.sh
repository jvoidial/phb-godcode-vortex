#!/data/data/com.termux/files/usr/bin/bash
# Grand National 2026 – Symbolic PHB / Energy / Resonance / Voxel Simulation
# NOTE: This is a symbolic simulation only – NOT a real‑world prediction.

PYTHON_BIN="${PYTHON_BIN:-python}"

$PYTHON_BIN << 'PYEOF'
import json
import math
import random
from datetime import datetime

# -----------------------------
# 1. Real runners (from document)
# -----------------------------
RUNNERS = [
    "Amirite",
    "Answer To Kayf",
    "Banbridge",
    "Beauport",
    "Captain Cody",
    "Champ Kiely",
    "Favori De Champdou",
    "Final Orders",
    "Firefox",
    "Gerri Colombe",
    "Gorgeous Tom",
    "Grangeclare West",
    "Haiti Couleurs",
    "High Class Hero",
    "I Am Maximus",
    "Imperial Saint",
    "Iroko",
    "Jagwar",
    "Johnnywho",
    "Jordans",
    "Lecky Watson",
    "Marble Sands",
    "Monty’s Star",
    "Mr Vango",
    "Oscar’s Brother",
    "Panic Attack",
    "Perceval Legallois",
    "Quai De Bourbon",
    "Spanish Harlem",
    "Stellar Story",
    "The Real Whacker",
    "Three Card Brag",
    "Top Of The Bill",
    "Twig",
]

# -----------------------------
# 2. Lightweight narrative hints (from your doc)
#    Used only to bias energy/resonance symbolically
# -----------------------------
NARRATIVE_HINTS = {
    "Panic Attack": {
        "form": 0.9,  # won Coral + Paddy Power
        "history": 0.5,
        "stamina": 0.8,
    },
    "I Am Maximus": {
        "form": 0.85,
        "history": 1.0,  # 1st + 2nd in previous Nationals
        "stamina": 0.9,
    },
    "Grangeclare West": {
        "form": 0.8,
        "history": 0.8,
        "stamina": 0.85,
    },
    "Jagwar": {
        "form": 0.8,
        "history": 0.4,
        "stamina": 0.75,
    },
    "Johnnywho": {
        "form": 0.78,
        "history": 0.4,
        "stamina": 0.8,
    },
    "Iroko": {
        "form": 0.75,
        "history": 0.8,  # 4th last year
        "stamina": 0.8,
    },
    "Haiti Couleurs": {
        "form": 0.7,
        "history": 0.7,
        "stamina": 0.85,
    },
    "Final Orders": {
        "form": 0.72,
        "history": 0.5,
        "stamina": 0.78,
    },
    "Gerri Colombe": {
        "form": 0.76,
        "history": 0.6,
        "stamina": 0.8,
    },
    # others will fall back to neutral defaults
}

# -----------------------------
# 3. Helper functions
# -----------------------------
def clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))

def make_voxel_grid(size=4, base_intensity=0.5, volatility=0.2, seed=None):
    if seed is not None:
        rnd = random.Random(seed)
    else:
        rnd = random
    n = size ** 3
    grid = []
    for i in range(n):
        noise = rnd.uniform(-volatility, volatility)
        val = clamp(base_intensity + noise)
        grid.append(round(val, 3))
    return grid

def build_runner_profile(name, idx):
    hint = NARRATIVE_HINTS.get(name, {})
    form = hint.get("form", 0.65)
    history = hint.get("history", 0.5)
    stamina = hint.get("stamina", 0.7)

    # random seed per runner for reproducible voxel pattern
    seed = hash(name) & 0xFFFFFFFF
    rnd = random.Random(seed)

    volatility = clamp(0.3 + rnd.uniform(-0.1, 0.1))
    base_energy = clamp(0.6 + 0.3 * (form - 0.65))
    coherence = clamp(0.6 + 0.3 * (history - 0.5))

    vox_base = clamp(0.5 * form + 0.3 * coherence - 0.2 * volatility)

    profile = {
        "name": name,
        "index": idx,
        "energy": {
            "base": round(base_energy, 3),
            "form_factor": round(form, 3),
            "stamina_factor": round(stamina, 3),
            "volatility": round(volatility, 3),
        },
        "resonance": {
            "coherence": round(coherence, 3),
            "history_weight": round(history, 3),
            "course_affinity": round(0.6 + 0.2 * history, 3),
            "field_interaction": round(0.6 + 0.2 * form, 3),
        },
        "voxels": {
            "grid_size": [4, 4, 4],
            "activation_pattern": "energy-resonance-derived",
            "intensity_map": make_voxel_grid(
                size=4,
                base_intensity=vox_base,
                volatility=volatility * 0.4,
                seed=seed,
            ),
        },
    }
    return profile

def race_phase_update(profile, phase):
    """Symbolic phase update: start / mid / final."""
    e = profile["energy"]
    r = profile["resonance"]

    phase_factor = {
        "start": 0.0,
        "mid": 0.5,
        "final": 1.0,
    }[phase]

    fatigue = 0.1 * phase_factor
    surge = 0.05 * (1.0 - e["volatility"]) * phase_factor

    new_stamina = clamp(e["stamina_factor"] - fatigue + surge)
    new_coherence = clamp(r["coherence"] - 0.05 * phase_factor + 0.03 * (e["form_factor"] - 0.65))

    e["stamina_factor"] = round(new_stamina, 3)
    r["coherence"] = round(new_coherence, 3)

    # adjust voxel base slightly
    base_intensity = clamp(0.5 * e["form_factor"] + 0.3 * r["coherence"] - 0.2 * e["volatility"])
    profile["voxels"]["intensity_map"] = make_voxel_grid(
        size=4,
        base_intensity=base_intensity,
        volatility=e["volatility"] * 0.4,
        seed=hash(profile["name"] + phase) & 0xFFFFFFFF,
    )

def compute_race_index(profile):
    e = profile["energy"]
    r = profile["resonance"]
    idx = (
        0.4 * e["stamina_factor"] +
        0.3 * r["coherence"] +
        0.2 * r["course_affinity"] -
        0.1 * e["volatility"]
    )
    return round(idx, 4)

# -----------------------------
# 4. Build profiles
# -----------------------------
profiles = [build_runner_profile(name, i+1) for i, name in enumerate(RUNNERS)]

# -----------------------------
# 5. Run symbolic race phases
# -----------------------------
phases = ["start", "mid", "final"]
for phase in phases:
    for p in profiles:
        race_phase_update(p, phase)

# -----------------------------
# 6. Compute symbolic ordering
# -----------------------------
results = []
for p in profiles:
    idx = compute_race_index(p)
    results.append((idx, p["name"]))

results.sort(reverse=True, key=lambda x: x[0])

symbolic_order = [name for _, name in results]

# -----------------------------
# 7. Build evolution packet
# -----------------------------
packet = {
    "engine": "PHB-GodCode-Vortex",
    "simulation": "Grand National 2026 – Symbolic Energy/Resonance/Voxel Model",
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "race": {
        "name": "Randox Grand National",
        "course": "Aintree",
        "scheduled_off": "2026-04-11T16:00:00+01:00",
        "going": "Good to Soft",
    },
    "runners": profiles,
    "symbolic_outcome": {
        "ordering": symbolic_order,
        "note": "This is a symbolic, internal codex ordering – NOT a real-world prediction or betting advice."
    }
}

# -----------------------------
# 8. Print to stdout + write JSON file
# -----------------------------
print("=== PHB SYMBOLIC GRAND NATIONAL 2026 SIMULATION ===")
print("Symbolic ordering (top 10):")
for i, name in enumerate(symbolic_order[:10], start=1):
    print(f"{i}. {name}")

out_path = "gcs/output/grand_national_2026_symbolic.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(packet, f, indent=2)

print(f"\n[PHB] Symbolic evolution packet written to: {out_path}")
print("[PHB] Reminder: This is NOT a prediction. Internal symbolic simulation only.")
PYEOF
