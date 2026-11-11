"""
One-command runner for the Concrete Strength Prediction project.

Usage (from the project root folder, in the VS Code terminal):
    python run_all.py

What it does, in order:
    1. Finds a compatible 64-bit Python (3.10 - 3.13, prefers 3.12 / 3.11)
       even if the Python you launched this with is too new or 32-bit
    2. Creates a local virtual environment (.venv); rebuilds it if it was
       made with an incompatible Python
    3. Installs the packages from requirements.txt (pre-built wheels only,
       so no C compiler / Visual Studio is ever needed)
    4. Runs Code/main.py (analysis -> preprocessing -> training -> evaluation)

Results (CSV tables and PNG graphs) are saved in the outputs/ folder.

When the run finishes, the saved graph images are opened automatically
in your default image viewer.

Optional:
    python run_all.py --no-open  # save the images but do not open them
    python run_all.py --show     # also show the live graph windows while running
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / ".venv"
REQUIREMENTS = ROOT / "requirements.txt"
MAIN_SCRIPT = ROOT / "Code" / "main.py"
OUTPUT_DIR = ROOT / "outputs"

MIN_VERSION = (3, 10)
MAX_VERSION = (3, 13)

PROBE = (
    "import sys, struct; "
    "print(sys.version_info[0], sys.version_info[1], struct.calcsize('P') * 8)"
)


def probe(cmd):
    """Return (major, minor, bits) for a Python command, or None if unusable."""
    try:
        out = subprocess.run(
            [str(c) for c in cmd] + ["-c", PROBE],
            capture_output=True, text=True, timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if out.returncode != 0:
        return None
    try:
        major, minor, bits = out.stdout.split()
        return int(major), int(minor), int(bits)
    except ValueError:
        return None


def is_compatible(info):
    if info is None:
        return False
    major, minor, bits = info
    return MIN_VERSION <= (major, minor) <= MAX_VERSION and bits == 64


def candidate_pythons():
    """Candidate interpreters in order of preference."""
    cands = []
    if os.name == "nt":
        cands += [["py", "-3.12-64"], ["py", "-3.11-64"]]
    else:
        for name in ("python3.12", "python3.11"):
            path = shutil.which(name)
            if path:
                cands.append([path])
    cands.append([sys.executable])
    if os.name == "nt":
        cands += [["py", "-3.13-64"], ["py", "-3.10-64"]]
    else:
        for name in ("python3.13", "python3.10"):
            path = shutil.which(name)
            if path:
                cands.append([path])
    return cands


def find_python():
    for cmd in candidate_pythons():
        if is_compatible(probe(cmd)):
            return cmd
    return None


def venv_python():
    if os.name == "nt":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def fail(message):
    print("\n" + "!" * 60)
    print(message)
    print("!" * 60)
    sys.exit(1)


def run(cmd, env=None):
    result = subprocess.run([str(c) for c in cmd], cwd=ROOT, env=env)
    return result.returncode


def open_images():
    """Open every PNG in outputs/ with the system's default image viewer."""
    images = sorted(OUTPUT_DIR.glob("*.png"))
    if not images:
        print("No images found in the outputs folder.")
        return
    print("Opening result images ...")
    for image in images:
        try:
            if os.name == "nt":
                os.startfile(str(image))
            elif sys.platform == "darwin":
                subprocess.Popen(["open", str(image)])
            else:
                subprocess.Popen(["xdg-open", str(image)])
            print("  opened:", image.name)
        except Exception as exc:
            print(f"  could not open {image.name}: {exc}")


def main():
    show_graphs = "--show" in sys.argv
    open_after = "--no-open" not in sys.argv

    print("=" * 50)
    print("Concrete Strength Prediction - Setup and Run")
    print("=" * 50)

    # Step 1: find a compatible Python
    print("\n[1/4] Looking for a compatible Python (64-bit, 3.10 - 3.13) ...")
    base_python = find_python()
    if base_python is None:
        fail(
            "No compatible Python was found.\n"
            "Please install 64-bit Python 3.12 from https://www.python.org/downloads/\n"
            "(tick 'py launcher' during installation), then run this script again."
        )
    major, minor, bits = probe(base_python)
    print(f"      Using Python {major}.{minor} ({bits}-bit)")

    # Step 2: virtual environment (rebuild if made with an incompatible Python)
    if venv_python().exists() and not is_compatible(probe([venv_python()])):
        print("\n[2/4] Existing .venv uses an incompatible Python - rebuilding ...")
        shutil.rmtree(VENV_DIR, ignore_errors=True)

    if venv_python().exists():
        print("\n[2/4] Virtual environment found.")
    else:
        print("\n[2/4] Creating virtual environment (.venv) ...")
        if run(base_python + ["-m", "venv", VENV_DIR]) != 0:
            fail("Could not create the virtual environment.")

    # Step 3: dependencies (wheels only: never tries to compile anything)
    print("\n[3/4] Installing dependencies (first run needs internet) ...")
    run([venv_python(), "-m", "pip", "install", "--upgrade", "pip", "-q"])
    code = run([
        venv_python(), "-m", "pip", "install",
        "--only-binary=:all:", "-r", REQUIREMENTS, "-q",
    ])
    if code != 0:
        fail(
            "Package installation failed.\n"
            "Check your internet connection and run the script again.\n"
            "If it still fails, install 64-bit Python 3.12 and retry."
        )

    # Step 4: run the project
    print("\n[4/4] Running the model ...\n")
    env = os.environ.copy()
    if not show_graphs:
        # Save graphs to files without opening windows that pause the script
        env["MPLBACKEND"] = "Agg"
    if run([venv_python(), MAIN_SCRIPT], env=env) != 0:
        fail("The model script failed. Read the error message above.")

    print("\n" + "=" * 50)
    print("DONE. Results are saved in:", OUTPUT_DIR)
    print("=" * 50)

    if open_after:
        open_images()


if __name__ == "__main__":
    main()
