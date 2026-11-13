import os

JOKE = ("I asked an AI coding agent for a joke about AI coding agents. It spun "
        "up three subagents, benchmarked the punchlines, and shipped the one "
        "with the highest eval score.")

def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out, "entry.txt")
    try:
        os.makedirs(out, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(JOKE + "\n")
    except OSError:
        fallback = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
        with open(fallback, "w", encoding="utf-8") as f:
            f.write(JOKE + "\n")
        path = fallback
    print("wrote", path)

if __name__ == "__main__":
    main()
