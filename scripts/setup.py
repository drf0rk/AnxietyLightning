#
# setup.py - The Project Downloader
# This script's only job is to download the project files from GitHub.
#
import subprocess
import shlex
import sys
from pathlib import Path

# --- Configuration ---
# The GitHub repository to download from. Format: 'user/repo'
REPO_URL = "drf0rk/AnxietyLightning"
# The branch to download.
BRANCH = "main"
# The destination directory.
DEST_DIR = Path("/content/ANXETY")

def run_command(command, description):
    """Runs a shell command and prints its status."""
    print(f"🔩 Executing: {description}...")
    try:
        process = subprocess.Popen(
            shlex.split(command),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        for line in iter(process.stdout.readline, ''):
            print(f"  > {line.strip()}")
        process.wait()
        if process.returncode == 0:
            print(f"✅ Success: {description} completed.")
            return True
        else:
            print(f"❌ Error: {description} failed with code {process.returncode}.")
            return False
    except FileNotFoundError:
        print(f"❌ Error: Command not found for '{description}'. Is the required tool installed?")
        return False
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return False

def main():
    """Main setup function."""
    print("--- Starting Project Setup ---")
    DEST_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Ensure degit is installed.
    # We first try to run it. If it fails, we assume it's not installed.
    if subprocess.run(['degit', '--version'], capture_output=True).returncode != 0:
        print("🔧 'degit' not found. Attempting to install via npm...")
        if not run_command("npm install -g degit", "Install degit"):
            print("❌ Critical error: Could not install degit. Please ensure npm is available.", file=sys.stderr)
            sys.exit(1)

    # 2. Download the repository.
    print(f"\nDownloading repository '{REPO_URL}'...")
    degit_command = f"degit {REPO_URL}#{BRANCH} {DEST_DIR} --force"
    if not run_command(degit_command, "Download repository files"):
        print("❌ Critical error: Failed to download repository files.", file=sys.stderr)
        sys.exit(1)
        
    print("\n✅ All project files have been downloaded successfully.")
    print("--- Project Setup Complete ---")

if __name__ == "__main__":
    main()