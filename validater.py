import sys
import importlib

# A list of all required packages for the game.
# The name here must match the module name used for import.
REQUIRED_PACKAGES = ["blessed", "perlin_noise"]

def check_dependencies():
    """
    Checks if all required Python modules can be imported.

    This function is designed to be imported by other scripts and does not
    print any output, returning a simple boolean status.

    Returns:
        bool: True if all dependencies are available, False otherwise.
    """
    for package_name in REQUIRED_PACKAGES:
        try:
            importlib.import_module(package_name)
        except ImportError:
            return False
    return True

def run_validation_and_print():
    """
    Runs the validation and prints a user-friendly report to the console.
    """
    print("--- Running Validation ---")
    all_found = True
    for package_name in REQUIRED_PACKAGES:
        try:
            importlib.import_module(package_name)
            print(f"  [OK] '{package_name}' module found.")
        except ImportError:
            print(f"  [ERROR] '{package_name}' module not found.")
            all_found = False

    print("-" * 26)
    if all_found:
        print("Validation successful! Environment is set up correctly.")
    else:
        print("\nValidation failed. Please run the installer script (installer.py).")
        sys.exit(1)


if __name__ == "__main__":
    run_validation_and_print()