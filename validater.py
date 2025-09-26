import os
import sys
import subprocess

# --- Configuration ---
VENV_DIR = ".venv"
REQUIREMENTS = ["blessed", "perlin_noise"]

# Determine the correct path for the venv Python executable
if sys.platform == "win32":
    VENV_PYTHON = os.path.join(VENV_DIR, "Scripts", "python.exe")
else:
    VENV_PYTHON = os.path.join(VENV_DIR, "bin", "python")

def run_validation():
    """
    Runs the validation process and prints a user-friendly report.
    """
    print("--- Running Validation ---")
    all_ok = True

    # 1. Check if the virtual environment exists
    print(f"1. Checking for virtual environment at '{VENV_DIR}'... ", end="")
    if not os.path.exists(VENV_PYTHON):
        print("FAILED")
        print(f"  - Python executable not found at: {os.path.abspath(VENV_PYTHON)}")
        all_ok = False
    else:
        print("OK")

    # 2. Check for required packages within the virtual environment
    if all_ok:
        print("2. Checking for required packages in .venv...")
        for package in REQUIREMENTS:
            print(f"  - Checking for '{package}'... ", end="")
            try:
                # We use the venv's python to try and import the package
                subprocess.run(
                    [VENV_PYTHON, "-c", f"import {package}"],
                    check=True,
                    capture_output=True,
                    text=True
                )
                print("OK")
            except (subprocess.CalledProcessError, FileNotFoundError):
                print("FAILED")
                all_ok = False

    print("-" * 28)
    if all_ok:
        print("Validation successful! Environment is set up correctly.")
    else:
        print("\nValidation failed. Please run option 3, 'Install Requirements', from the main menu.")
        # We exit with a non-zero code to indicate failure, though the batch file will pause anyway.
        sys.exit(1)

if __name__ == "__main__":
    run_validation()