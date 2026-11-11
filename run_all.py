"""
One-command runner for the Concrete Strength Prediction project.

Usage (from the project root folder, in the VS Code terminal):
    python run_all.py

What it does, in order:
    1. Creates a local virtual environment (.venv) if it does not exist
    2. Installs the packages from requirements.txt
    3. Runs Code/main.py (analysis -> preprocessing -> training -> evaluation)

Results (CSV tables and PNG graphs) are saved in the outputs/ folder.

Optional:
    python run_all.py --show     # also open the graph windows while running
"""

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / ".venv"
REQUIREMENTS = ROOT / "requirements.txt"
MAIN_SCRIPT = ROOT / "Code" / "main.py"
OUTPUT_DIR = ROOT / "outputs"


def venv_python() -> Path:
    if os.name == "nt":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def run(cmd, env=None):
    result = subprocess.run([str(c) for c in cmd], cwd=ROOT, env=env)
    if result.returncode != 0:
        print(f"\nCommand failed: {' '.join(str(c) for c in cmd)}")
        sys.exit(result.returncode)


def main():
    show_graphs = "--show" in sys.argv

    print("=" * 50)
    print("Concrete Strength Prediction - Setup and Run")
    print("=" * 50)

    # Step 1: virtual environment
    if venv_python().exists():
        print("\n[1/3] Virtual environment found.")
    else:
        print("\n[1/3] Creating virtual environment (.venv) ...")
        run([sys.executable, "-m", "venv", VENV_DIR])

    # Step 2: dependencies
    print("\n[2/3] Installing dependencies ...")
    run([venv_python(), "-m", "pip", "install", "--upgrade", "pip", "-q"])
    run([venv_python(), "-m", "pip", "install", "-r", REQUIREMENTS, "-q"])

    # Step 3: run the project
    print("\n[3/3] Running the model ...\n")
    env = os.environ.copy()
    if not show_graphs:
        # Save graphs to files without opening windows that pause the script
        env["MPLBACKEND"] = "Agg"
    run([venv_python(), MAIN_SCRIPT], env=env)

    print("\n" + "=" * 50)
    print("DONE. Results are saved in:", OUTPUT_DIR)
    print("=" * 50)


if __name__ == "__main__":
    main()
