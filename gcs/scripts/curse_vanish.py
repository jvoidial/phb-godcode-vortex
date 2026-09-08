# curse_vanish.py - Symbolic Curse Cleansing Engine
# Uses PHB coherence/voxel/energy systems

import json
import time
import random
from datetime import datetime

class CurseVanishEngine:
    def __init__(self):
        self.state_file = "gcs/network_state.json"
        self.log_file = "gcs/cleansing_log.txt"
        
    def scan_energy(self):
        """Scans for symbolic curse signatures"""
        try:
            with open(self.state_file, 'r') as f:
                state = json.load(f)
        except:
            state = {"coherence": 1.0, "voxels": [], "energy": 0}
        
        # Symbolic curse detection based on coherence decay
        curse_detected = False
        if state.get("coherence", 1.0) < 0.5:
            curse_detected = True
        if len(state.get("voxels", [])) > 100:
            curse_detected = True
            
        return curse_detected, state
    
    def vanish_curse(self):
        """Performs symbolic curse removal"""
        detected, state = self.scan_energy()
        
        if not detected:
            print("✨ No curse signatures detected. You are clear.")
            return
            
        print("🔮 Curse detected! Beginning vanish protocol...")
        time.sleep(1)
        
        # Reset coherence to full strength
        state["coherence"] = 1.0
        
        # Clear corrupted voxels
        state["voxels"] = [v for v in state.get("voxels", []) if v.get("pure", True)]
        
        # Reset energy threshold
        state["energy"] = 100.0
        
        # Add cleansing timestamp
        state["last_cleansing"] = datetime.now().isoformat()
        
        # Generate protection key
        key = random.randint(10000, 99999)
        state["protection_key"] = key
        
        # Save new state
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=2)
            
        # Log the event
        with open(self.log_file, 'a') as f:
            f.write(f"CURSE VANISHED: {datetime.now()} | Key: {key}\n")
            
        print(f"✅ Curse vanished! Protection Key: {key}")
        print("🛡️ Coherence restored, voxels purified, energy at 100%")
        print("📝 Log saved to cleansing_log.txt")

if __name__ == "__main__":
    engine = CurseVanishEngine()
    engine.vanish_curse()
