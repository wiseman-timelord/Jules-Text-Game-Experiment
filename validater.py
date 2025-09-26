import sys

# A list of all required packages for the game.
REQUIRED_PACKAGES = ["blessed", "perlin_noise"]

def validate_installation():
    """
    Validates that all required modules can be imported.
    """
    print("Validating required modules...")
    all_found = True
    for package in REQUIRED_PACKAGES:
        try:
            # The 'import' statement uses the module name, which can sometimes
            # differ from the package name (e.g., perlin-noise vs perlin_noise).
            __import__(package)
            print(f"  [OK] '{package}' module found.")
        except ImportError:
            print(f"  [ERROR] '{package}' module not found.")
            all_found = False

    return all_found

if __name__ == "__main__":
    print("--- Running Validation ---")
    if validate_installation():
        print("\nEnvironment is set up correctly.")
    else:
        print("\nValidation failed. Please run the installer script (installer.py) to install missing packages.")
        sys.exit(1)