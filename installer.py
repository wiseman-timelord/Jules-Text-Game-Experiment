import os
import sys
import json
import shutil
import subprocess
import venv

# ------------------------------------------------------------------
#  Paths – adjust if your project layout is different
# ------------------------------------------------------------------
VENV_DIR   = ".venv"
SETTINGS = os.path.join("data", "settings.json")
SETTINGS_TEMPLATE = {"volume": 0.8, "debug": False}   # example content

# ------------------------------------------------------------------
#  Helper – cross-platform “press any key”
# ------------------------------------------------------------------
def wait_key():
    """Block until the user presses a key."""
    if os.name == "nt":
        os.system("pause >nul")
    else:
        input("Press ENTER to return to the menu…")

# ------------------------------------------------------------------
#  Helper – run a command, stream stdout / stderr live
# ------------------------------------------------------------------
def run_stream(cmd, *, check=True):
    """Run cmd and echo its output in real time (no capture)."""
    try:
        subprocess.run(cmd, check=check)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Command failed: {' '.join(cmd)}")
        raise e

# ------------------------------------------------------------------
#  Main installation routine
# ------------------------------------------------------------------
def install_requirements():
    """Full re-install: clean settings, fresh venv, pip + packages."""

    # --- 1.  Clear console and show new banner -----------------------------
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 79)
    print("    Jules' Text Adventure Game - Installation")
    print("=" * 79, "")

    # --- 2.  Manage settings.json -----------------------------------------
    print(f"Managing '{SETTINGS}'...")
    if os.path.isfile(SETTINGS):
        os.remove(SETTINGS)
        print(f"Replaced '{SETTINGS}'.")
    os.makedirs(os.path.dirname(SETTINGS), exist_ok=True)
    with open(SETTINGS, "w", encoding="utf-8") as fh:
        json.dump(SETTINGS_TEMPLATE, fh, indent=2)

    # --- 3.  Remove old venv ----------------------------------------------
    print("Cleaning up old virtual environment ('.venv')...")
    if os.path.isdir(VENV_DIR):
        shutil.rmtree(VENV_DIR)
        print("Removed existing '.venv' directory.")
    else:
        print("No existing '.venv' directory found. Skipping.")

    # --- 4.  Create new venv ----------------------------------------------
    print("Creating new virtual environment via subprocess...")
    try:
        # Use the same Python executable that is running this script to create the venv.
        run_stream([sys.executable, "-m", "venv", VENV_DIR])
        print(".venv directory Created... OK")
    except subprocess.CalledProcessError:
        print("\n[CRITICAL ERROR] Failed to create virtual environment.")
        sys.exit(1)

    # --- 5.  Determine python / pip inside venv ---------------------------
    if os.name == "nt":                       # Windows
        venv_python = os.path.join(VENV_DIR, "Scripts", "python.exe")
        venv_pip    = os.path.join(VENV_DIR, "Scripts", "pip.exe")
    else:                                     # macOS / Linux
        venv_python = os.path.join(VENV_DIR, "bin", "python")
        venv_pip    = os.path.join(VENV_DIR, "bin", "pip")

    # --- 5a. Verify venv creation ---
    if not os.path.exists(venv_python):
        print("\n[CRITICAL ERROR] Virtual environment creation failed.")
        print(f"Python executable not found at: {os.path.abspath(venv_python)}")
        sys.exit(1)

    # --- 6.  Upgrade pip ---------------------------------------------------
    print("\nUpgrading pip to latest version...")
    run_stream([venv_python, "-m", "pip", "install", "--upgrade", "pip"])

    # --- 7.  Install packages ---------------------------------------------
    print("\nInstalling requirements...")
    run_stream([venv_pip, "install", "blessed", "perlin-noise"])

    # --- 8.  Final report --------------------------------------------------
    print("\n--- Installation Report ---")
    print("All steps completed successfully!")
    print(f"Virtual environment created at: {os.path.abspath(VENV_DIR)}")
    print("Required packages installed: blessed, perlin-noise")
    print("You can now run the game using option 1 from the main menu.")
    print("-" * 59)
    print("\n" + "-" * 79)

# Entry point
if __name__ == "__main__":
    install_requirements()