import sys
import os

# This allows the launcher to find the 'scripts' and 'validater' modules
sys.path.append(os.path.dirname(__file__))
from validater import check_dependencies

def main():
    """
    The main entry point for the game.
    This function validates the environment before attempting to run the game.
    """
    print("Launcher is running...")

    # --- Pre-launch Validation ---
    print("Checking for required packages...")
    if not check_dependencies():
        print("\n[ERROR] Required packages are missing.")
        print("Please run 'installer.py' to set up the environment, then try again.")
        # Add a pause for Windows users running the .bat file
        if sys.platform == "win32":
            os.system("pause")
        sys.exit(1)

    print("All packages found. Attempting to start the game.")

    try:
        # We can now be more confident that the game will import correctly.
        from scripts import game
        game.start()
    except ImportError as e:
        print(f"\n[CRITICAL ERROR] Failed to import game modules: {e}")
        print("The game files appear to be corrupted or missing. Please check your installation.")
        if sys.platform == "win32":
            os.system("pause")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred during gameplay: {e}")
        if sys.platform == "win32":
            os.system("pause")
        sys.exit(1)

if __name__ == "__main__":
    main()