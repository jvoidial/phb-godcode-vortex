#!/data/data/com.termux/files/usr/bin/bash
# Grand National 2026 – Dual Engine Simulation:
# PHB Energy/Resonance/Voxels + Weather Modulation Layer
# NOT a prediction. Symbolic codex simulation only.

PYTHON_BIN="${PYTHON_BIN:-python}"

$PYTHON_BIN << 'PYEOF'
import json, random, math
from datetime import datetime, timezone

# -----------------------------
# REAL RUNNERS (from your document)
# -----------------------------
RUNNERS = [
    "Amirite","Answer To Kayf","Banbridge","Beauport","Captain Cody","Champ Kiely",
    "Favori De Champdou","Final Orders","Firefox","Gerri Colombe","Gorgeous Tom",
    "Grangeclare West","Haiti Couleurs","High Class Hero","I Am Maximus",
    "Imperial Saint","Iroko","Jagwar","Johnnywho","Jordans","Lecky Watson",
    "Marble Sands","Monty’s Star","Mr Vango","Oscar’s Brother","Panic Attack",
    "Perceval Legallois","Quai De Bourbon","Spanish Harlem","Stellar Story",
    "The Real Whacker","Three Card Brag","Top Of The Bill","Twig"
]

# -----------------------------
# WEATHER CONDITIONS (symbolic)
# -----------------------------
WEATHER = {
    "temperature_c": 11.0,
    "humidity": 0.72,
    "wind_speed_mph": 14,
    "wind_direction": "SW",
    "rain_mm": 0.8,
    "going": "Good to Soft",
    "atmospheric_pressure": 1009
}

# Convert weather → symbolic modifiers
def weather_modifiers():
    # Lower pressure → more chaos
    pressure_factor = max(0.0, min(1.0, (WEATHER["atmospheric_pressure"] - 995) / 25))

    # Rain softens ground → stamina bias
    rain_factor = min(1.0, WEATHER["rain_mm"] / 5)

    # Wind → volatility
    wind_factor = min(1.0, WEATHER["wind_speed_mph"] / 30)

    return {
        "stamina_bonus": 0.05 * rain_factor,
        "coherence_penalty": 0.04 * wind_factor,
        "volatility_bonus": 0.06 * wind_factor,
        "pressure_instability": 0.05 * (1 - pressure_factor)
    }

W_MOD = weather_modifiers()

# -----------------------------
# PHB ENERGY/RESONANCE MODEL
# -----------------------------
def clamp(x): return max(0.0, min(1.0, x))

def build_profile(name):
    seed = hash(name) & 0xFFFFFFFF
    rnd = random.Random(seed)

    base = 0.55 + rnd.uniform(-0.1, 0.1)
    form = 0.6 + rnd.uniform(-0.15, 0.15)
    stamina = 0.65 + rnd.uniform(-0.15, 0.15)
    volatility = 0.3 + rnd.uniform(-0.1, 0.1)
    coherence = 0.6 + rnd.uniform(-0.15, 0.15)

    # Apply weather modulation
    stamina = clamp(stamina + W_MOD["stamina_bonus"])
    coherence = clamp(coherence - W_MOD["coherence_penalty"])
    volatility = clamp(volatility + W_MOD["volatility_bonus"] + W_MOD["pressure_instability"])

    return {
        "name": name,
        "energy": {
            "base": round(base,3),
            "form_factor": round(form,3),
            "stamina_factor": round(stamina,3),
            "volatility": round(volatility,3)
        },
        "resonance": {
            "coherence": round(coherence,3),
            "course_affinity": round(0.55 + rnd.uniform(-0.1,0.1),3)
        }
    }

def race_index(p):
    e = p["energy"]
    r = p["resonance"]
    return round(
        0.35*e["stamina_factor"] +
        0.25*r["coherence"] +
        0.2*r["course_affinity"] -
        0.2*e["volatility"],
        4
    )

# -----------------------------
# BUILD PROFILES
# -----------------------------
profiles = [build_profile(n) for n in RUNNERS]

# -----------------------------
# COMPUTE SYMBOLIC ORDERING
# -----------------------------
ordering = sorted(
    [(race_index(p), p["name"]) for p in profiles],
    reverse=True
)

symbolic_order = [name for _, name in ordering]

# -----------------------------
# OUTPUT
# -----------------------------
print("=== PHB DUAL-ENGINE SIMULATION (WEATHER + ENERGY/RESONANCE) ===")
print("Top 10 symbolic ordering:")
for i, name in enumerate(symbolic_order[:10], start=1):
    print(f"{i}. {name}")

# Save JSON
import os
os.makedirs("gcs/output", exist_ok=True)

packet = {
    "engine": "PHB Dual Engine",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "weather": WEATHER,
    "modifiers": W_MOD,
    "symbolic_order": symbolic_order,
    "profiles": profiles,
    "note": "Symbolic codex simulation only. Not a real-world prediction."
}

with open("gcs/output/grand_national_2026_weather_symbolic.json","w") as f:
    json.dump(packet,f,indent=2)

print("\n[PHB] Weather‑modulated symbolic packet saved to:")
print("gcs/output/grand_national_2026_weather_symbolic.json")
PYEOF
