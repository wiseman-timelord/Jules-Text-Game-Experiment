import os
import sys
import subprocess
import shutil

# --- Configuration ---
VENV_DIR = ".venv"
DATA_DIR = "data"
SETTINGS_FILE = os.path.join(DATA_DIR, "settings.json")
REQUIREMENTS = ["blessed", "perlin-noise"]

# Determine the correct paths for the venv executables based on the OS
if sys.platform == "win32":
    VENV_PYTHON = os.path.join(VENV_DIR, "Scripts", "python.exe")
    VENV_PIP = os.path.join(VENV_DIR, "Scripts", "pip.exe")
else:
    VENV_PYTHON = os.path.join(VENV_DIR, "bin", "python")
    VENV_PIP = os.path.join(VENV_DIR, "bin", "pip")

def run_silent_command(command, description):
    """Runs a command silently and handles errors, printing a status message."""
    print(f"  - {description}... ", end="")
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        print("OK")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print("FAILED")
        if isinstance(e, subprocess.CalledProcessError):
            print("\n--- ERROR ---")
            print(e.stderr)
            print("---------------")
        return False

def run_verbose_command(command, description):
    """Runs a command and streams its output to the console."""
    print(f"  - {description}:")
    print("-" * 20)
    try:
        # By not capturing output, it streams directly to the console.
        subprocess.run(command, check=True)
        print("-" * 20)
        print("  - Command successful.")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\n--- COMMAND FAILED ---")
        # The error is already printed by the subprocess, so we just note the failure.
        return False

def manage_settings_file():
    """Step 1 & 5: Ensure a clean settings.json file exists."""
    print(f"1. Managing '{SETTINGS_FILE}'...")
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        if os.path.exists(SETTINGS_FILE):
            os.remove(SETTINGS_FILE)
            print(f"  - Removed existing '{SETTINGS_FILE}'.")

        with open(SETTINGS_FILE, 'w') as f:
            f.write('{\n  "message": "Settings loaded correctly."\n}\n')
        print(f"  - Created clean '{SETTINGS_FILE}'.")
        return True
    except Exception as e:
        print(f"  - FAILED to manage settings file: {e}")
        return False

def clean_venv():
    """Step 2: Remove the existing virtual environment if it exists."""
    print(f"2. Cleaning up old virtual environment ('{VENV_DIR}')...")
    if os.path.exists(VENV_DIR):
        try:
            shutil.rmtree(VENV_DIR)
            print(f"  - Removed existing '{VENV_DIR}' directory.")
        except Exception as e:
            print(f"  - FAILED to remove '{VENV_DIR}': {e}")
            return False
    else:
        print(f"  - No existing '{VENV_DIR}' directory found. Skipping.")
    return True

def create_venv():
    """Step 3: Create the virtual environment."""
    print("3. Creating new virtual environment...")
    return run_silent_command(
        [sys.executable, "-m", "venv", VENV_DIR],
        "Creating .venv directory"
    )

def upgrade_pip():
    """Step 3 (cont.): Upgrade pip in the new virtual environment."""
    print("4. Upgrading pip...")
    return run_verbose_command(
        [VENV_PYTHON, "-m", "pip", "install", "--upgrade", "pip"],
        "Upgrading pip to the latest version"
    )

def install_requirements():
    """Step 4: Install required libraries into the virtual environment."""
    print("5. Installing required packages...")
    return run_verbose_command(
        [VENV_PIP, "install"] + REQUIREMENTS,
        f"Installing {', '.join(REQUIREMENTS)}"
    )

def main():
    """Main function to run the full installation process."""
    print("--- Running Full Installation and Setup ---")

    steps = [
        manage_settings_file,
        clean_venv,
        create_venv,
        upgrade_pip,
        install_requirements
    ]

    all_successful = True
    for i, step_func in enumerate(steps, 1):
        if not step_func():
            print(f"\n[ERROR] Step {i} ('{step_func.__name__}') failed. Aborting installation.")
            all_successful = False
            break
        print("\n")

    print("--- Installation Report ---")
    if all_successful:
        print("All steps completed successfully!")
        print(f"Virtual environment created at: {os.path.abspath(VENV_DIR)}")
        print(f"Required packages installed: {', '.join(REQUIREMENTS)}")
        print("You can now run the game using option 1 from the main menu.")
    else:
        print("Installation failed. Please review the errors above.")
    print("---------------------------\n")
    if not all_successful:
        sys.exit(1)

if __name__ == "__main__":
    main()