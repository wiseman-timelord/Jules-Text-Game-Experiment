import sys
import os

# This allows the launcher to find the 'scripts' module.
# We must add the root directory to the path for this to work correctly.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    """
    The main entry point for the game. This function simply
    imports and runs the main game module.
    """
    try:
        from scripts import game
        game.start()
    except ImportError as e:
        print("\n[CRITICAL ERROR] Failed to launch the game.")
        print(f"A required module could not be found: {e}")
        print("This is likely due to missing dependencies.")
        print("Please run option 3, 'Install Requirements', from the main menu and try again.")
        if 'win32' in sys.platform:
            os.system("pause")
    except Exception as e:
        print(f"\nAn unexpected error occurred during gameplay: {e}")
        if 'win32' in sys.platform:
            os.system("pause")

if __name__ == "__main__":
    main()