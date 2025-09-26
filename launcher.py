import sys
import os

# This allows the launcher to find the 'scripts' module
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

def main():
    """
    The main entry point for the game.
    This function will initialize and run the main game loop.
    """
    print("Launcher is running...")
    print("Attempting to start the game.")

    try:
        # We will import and run the game from the 'scripts' directory
        # This will fail for now, as game.py doesn't exist yet.
        # We will create it in the next step.
        import game
        game.start()
    except ImportError:
        print("\nError: 'game.py' not found in the 'scripts' directory.")
        print("This is expected if the game files have not been created yet.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()