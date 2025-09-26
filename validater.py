import sys

REQUIRED_PACKAGE = "blessed"

def validate_installation():
    """
    Validates that the required 'blessed' module can be imported.
    """
    print(f"Validating '{REQUIRED_PACKAGE}' module availability...")
    try:
        import blessed
        print(f"Validation successful: '{REQUIRED_PACKAGE}' module can be imported.")
        return True
    except ImportError:
        print(f"\nError: The '{REQUIRED_PACKAGE}' module could not be imported.")
        print(f"Please run the installer script (installer.py) to install '{REQUIRED_PACKAGE}'.")
        return False

if __name__ == "__main__":
    print("--- Running Validation ---")
    if validate_installation():
        print("\nEnvironment is set up correctly.")
    else:
        print("\nValidation failed. Please review the errors above.")
        sys.exit(1)