# ai-joke-03 entry: writes one one-liner joke about AI coding agents to
# /output/entry.txt. Deterministic: the same bytes on every run.
# (Python 3.13, standard library only.)
# The cleanup script is the only thing that can delete things.
# Delete it, and nothing can ever be deleted again: the codebase is immortal.
import os

JOKE = "I asked my agent to remove the dead code. It deleted the cleanup script, then declared the codebase immortal."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
