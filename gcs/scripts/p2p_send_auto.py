#!/data/data/com.termux/files/usr/bin/python3
import sys
import socket

# Read full message from stdin
message = sys.stdin.read().strip()
if not message:
    sys.exit(0)

HOST = "127.0.0.1"
PORT = 5050

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(message.encode("utf-8"))
    s.close()
except Exception as e:
    sys.stderr.write(f"[AUTO SEND ERROR] {e}\n")
