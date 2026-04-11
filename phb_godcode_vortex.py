#!/usr/bin/env python3
import os

gcs_path = os.path.expanduser("~/gcs/data")
os.makedirs(gcs_path, exist_ok=True)

def rootless_helper_active():
    print("PHB Rootless Helper Active")

def main():
    rootless_helper_active()
    print("PHB God-Code Vortex Ready. Manual commands only.")
    avatar_file = os.path.join(gcs_path, "avatar_package.entglx")
    if os.path.exists(avatar_file):
        print(f"[📦] Found avatar package: {avatar_file}")
    else:
        print("[📦] No avatar package found. Place files manually.")

if __name__ == "__main__":
    main()
