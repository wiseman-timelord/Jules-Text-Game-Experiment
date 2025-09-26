import subprocess
import sys

# The 'blessed' library is required for the game's terminal interface.
# It works across different platforms.
REQUIRED_PACKAGE = "blessed"

def install_packages():
    """
    Installs the necessary 'blessed' package directly to the system's Python environment.
    """
    print(f"Attempting to install '{REQUIRED_PACKAGE}'...")
    try:
        # Use the current Python interpreter's pip to install the package.
        # The --no-input flag prevents pip from prompting for input.
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--no-input", REQUIRED_PACKAGE],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Successfully installed '{REQUIRED_PACKAGE}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing '{REQUIRED_PACKAGE}': {e}")
        print(f"STDOUT: {e.stdout}")
        print(f"STDERR: {e.stderr}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: 'pip' could not be found. Is Python installed correctly?")
        sys.exit(1)


if __name__ == "__main__":
    print("--- Running Installer ---")
    install_packages()
    print("\nInstallation process complete.")