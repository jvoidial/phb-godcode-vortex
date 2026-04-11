import sys
from pathlib import Path

LOG_PATH = Path("phb_godcode_vortex_log.txt")

def main():
    if not LOG_PATH.exists():
        sys.stderr.write("No phb_godcode_vortex_log.txt found\n")
        sys.exit(1)

    text = LOG_PATH.read_text(encoding="utf-8", errors="ignore")

    marker = "FINAL JSON DUMP"
    idx = text.rfind(marker)
    if idx == -1:
        sys.stderr.write("No FINAL JSON DUMP block found in log\n")
        sys.exit(1)

    chunk = text[idx:]
    brace_idx = chunk.find("{")
    if brace_idx == -1:
        sys.stderr.write("No JSON brace found after FINAL JSON DUMP\n")
        sys.exit(1)

    json_str = chunk[brace_idx:].strip()
    # Output the JSON as-is; receiver can parse it
    print(json_str)

if __name__ == "__main__":
    main()
