# /scripts/setup.py - The Project Downloader (v2 - Robust Checks)
# This script's only job is to download the project files from GitHub.

import subprocess
import shlex
import sys
from pathlib import Path

# --- Configuration ---
REPO_URL = "drf0rk/AnxietyLightning"
BRANCH = "main"
DEST_DIR = Path("/content/ANXETY")

def run_command(command, description):
    """Runs a shell command and prints its status."""
    print(f"🔩 Executing: {description}...")
    try:
        process = subprocess.Popen(
            shlex.split(command),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        while True:
            line = process.stdout.readline()
            if not line:
                break
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

def check_command_exists(command):
    """Safely checks if a command exists without crashing."""
    try:
        subprocess.run([command, '--version'], capture_output=True, check=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

def main():
    """Main setup function."""
    print("--- Starting Project Setup ---")
    DEST_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Ensure npm and degit are installed.
    if not check_command_exists('npm'):
         if not run_command("apt-get -y install nodejs npm", "Install npm"):
             print("❌ Critical error: Could not install npm.", file=sys.stderr)
             sys.exit(1)

    if not check_command_exists('degit'):
        print("🔧 'degit' not found. Attempting to install via npm...")
        if not run_command("npm install -g degit", "Install degit"):
            print("❌ Critical error: Could not install degit.", file=sys.stderr)
            sys.exit(1)

    # 2. Download the repository using degit.
    print(f"\nDownloading repository '{REPO_URL}'...")
    degit_command = f"degit {REPO_URL}#{BRANCH} {DEST_DIR} --force"
    if not run_command(degit_command, "Download repository files"):
        print("❌ Critical error: Failed to download repository files.", file=sys.stderr)
        sys.exit(1)
        
    print("\n✅ All project files have been downloaded successfully.")
    print("--- Project Setup Complete ---")

if __name__ == "__main__":
    main()
