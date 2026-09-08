#!/bin/bash
echo "🧠 AGI AUTO-LOOP ACTIVATED"

while true; do
  echo "$(date): AGI cycle running..."
  
  # Update AGI brain
  python3 ~/phb-godcode-vortex/ecosystem/agi-learning/agi_brain_update.py 2>/dev/null
  
  # Run wealth cycle
  python3 ~/eco-warrior/auto-rich/auto_rich.py 2>/dev/null
  
  echo "$(date): Cycle complete. Sleeping 1 hour..."
  sleep 3600
done
