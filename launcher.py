import os
import sys
import subprocess

# --- Configuration ---
VENV_DIR = ".venv"
GAME_SCRIPT = os.path.join("scripts", "game.py")

# Determine the correct path for the venv Python executable
if sys.platform == "win32":
    VENV_PYTHON = os.path.join(VENV_DIR, "Scripts", "python.exe")
else:
    VENV_PYTHON = os.path.join(VENV_DIR, "bin", "python")

def main():
    """
    Launches the game using the Python interpreter from the virtual environment.
    """
    # 1. Check if the venv python executable exists.
    if not os.path.exists(VENV_PYTHON):
        print("\n[CRITICAL ERROR] Virtual environment not found.")
        print(f"Looked for: {os.path.abspath(VENV_PYTHON)}")
        print("Please run option 3, 'Install Requirements', from the main menu.")
        if 'win32' in sys.platform:
            os.system("pause")
        sys.exit(1)

    # 2. Check if the main game script exists.
    if not os.path.exists(GAME_SCRIPT):
        print(f"\n[CRITICAL ERROR] Game script not found at '{GAME_SCRIPT}'.")
        print("The game files appear to be corrupted or missing.")
        if 'win32' in sys.platform:
            os.system("pause")
        sys.exit(1)

    # 3. Launch the game using the venv's python.
    # We run this in a subprocess. This launcher script's job is just to
    # kick off the game with the right interpreter.
    try:
        # The `subprocess.run` call will wait here until the game exits.
        subprocess.run([VENV_PYTHON, GAME_SCRIPT], check=True)
    except subprocess.CalledProcessError as e:
        # This will catch errors if the game script itself crashes.
        # The game script has its own error handling, but this is a fallback.
        print(f"\nAn error occurred while running the game: {e}")
        if 'win32' in sys.platform:
            os.system("pause")
    except FileNotFoundError:
        # This is a fallback in case VENV_PYTHON is not found at the last second.
        print(f"\n[CRITICAL ERROR] Could not execute Python from the virtual environment.")
        print(f"Path may be incorrect: {os.path.abspath(VENV_PYTHON)}")
        if 'win32' in sys.platform:
            os.system("pause")
        sys.exit(1)

if __name__ == "__main__":
    main()