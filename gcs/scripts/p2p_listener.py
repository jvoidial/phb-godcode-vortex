#!/data/data/com.termux/files/usr/bin/python3
import socket
import json
import sys
from pathlib import Path

HOST = "127.0.0.1"
PORT = 5050

print("[GCS LISTENER] Starting listener...")

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow immediate reuse of the port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    s.bind((HOST, PORT))
except OSError as e:
    print(f"[GCS LISTENER] ERROR: {e}")
    sys.exit(1)

s.listen(5)
print(f"[GCS LISTENER] Listening on {HOST}:{PORT}")

while True:
    conn, addr = s.accept()
    data = conn.recv(65535).decode("utf-8").strip()

    if not data:
        conn.close()
        continue

    # Try to parse JSON
    try:
        parsed = json.loads(data)
        print("[GCS LISTENER] JSON received (PHB evolution packet)")

        # Save to shared network state
        Path("gcs/network_state.json").write_text(
            json.dumps(parsed, indent=2),
            encoding="utf-8"
        )

        conn.sendall(b"[GCS LISTENER] OK: JSON stored\n")
        conn.close()
        continue

    except json.JSONDecodeError:
        pass

    # Fallback for non-JSON messages
    print(f"[GCS LISTENER] TEXT received: {data}")
    conn.sendall(b"[GCS LISTENER] OK: TEXT received\n")
    conn.close()
