# **PHB God‑Code Vortex**  
### *A distributed, evolving symbolic engine with real‑time P2P synchronisation*

---

## 📌 Overview

PHB God‑Code Vortex is a **modular, evolving symbolic engine** that generates:

- Coherence & Stability curves  
- Codex Pages  
- Voxel layers  
- Veil simulator states  
- Energy signatures  
- Portal states  
- Full JSON evolution packets  

The system includes a **P2P network layer** that allows multiple Termux devices to:

- broadcast their PHB evolution JSON  
- receive evolution packets from peers  
- store shared state in `gcs/network_state.json`  
- evolve together in real time  

This creates a **distributed Codex organism**.

---

# 📥 Installation (Termux)

### 1. Clone the repository

\`\`\`
git clone https://github.com/jvoidial/phb-godcode-vortex.git
cd phb-godcode-vortex
\`\`\`

### 2. Run the installer

\`\`\`
bash installer.sh
\`\`\`

This will:

- update Termux  
- install Python + git  
- sync the repository  
- prepare the P2P layer  
- create required directories  
- ensure all scripts are executable  
- create \`network_state.json\` if missing  

---

# ▶️ Running the System

\`\`\`
./gcs/run_phb_p2p.sh
\`\`\`

This will:

1. Run the PHB engine  
2. Start the P2P listener  
3. Auto‑extract FINAL JSON  
4. Auto‑broadcast to peers  
5. Store incoming JSON in \`gcs/network_state.json\`  

---

# 🌐 Multi‑Device Evolution

Every device running:

\`\`\`
./gcs/run_phb_p2p.sh
\`\`\`

will:

- generate its own PHB evolution  
- broadcast JSON  
- receive JSON  
- update shared state  

This forms a **distributed symbolic mesh**.

---

# 📁 Project Structure

\`\`\`
phb-godcode-vortex/
├── installer.sh
├── gcs/
│   ├── run_phb_p2p.sh
│   ├── network_state.json
│   ├── phb_auto_broadcast.py
│   └── scripts/
│       ├── p2p_listener.py
│       ├── p2p_send_auto.py
│       └── p2p_send.py
└── engine/
\`\`\`

---

# 🧙‍♂️ Author

Jacob — creator of the PHB symbolic engine and distributed Codex mesh.
