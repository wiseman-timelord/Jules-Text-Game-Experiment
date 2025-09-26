import subprocess
import sys

# The required packages for the game.
# 'blessed' is for the terminal interface.
# 'perlin-noise' is for procedural map generation.
REQUIRED_PACKAGES = ["blessed", "perlin-noise"]

def install_packages():
    """
    Installs the necessary packages directly to the system's Python environment.
    """
    print("Attempting to install required packages...")
    try:
        # Use the current Python interpreter's pip to install the packages.
        # The --no-input flag prevents pip from prompting for input.
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--no-input"] + REQUIRED_PACKAGES,
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Successfully installed: {', '.join(REQUIRED_PACKAGES)}.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {e}")
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