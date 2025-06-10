# /content/ANXETY/scripts/UIs/ReForge.py (Definitive Final Version)

import os
import sys
from pathlib import Path
import subprocess

# --- Self-aware pathing ---
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[2]
except NameError:
    ANXETY_ROOT = Path.cwd()
if str(ANXETY_ROOT) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT))
sys.path.insert(0, str(ANXETY_ROOT / 'modules'))
# ---

from Manager import m_download

# Constants
UI = 'ReForge'
HOME = Path.home()
WEBUI_PATH = HOME / UI
REPO_URL = f"https://huggingface.co/NagisaNao/ANXETY/resolve/main/{UI}.zip"

def main():
    if not WEBUI_PATH.exists():
        print(f"✅ Downloading and unpacking {UI} from Hugging Face...")
        zip_path = HOME / f"{UI}.zip"
        
        m_download(f'"{REPO_URL}" "{HOME}" "{zip_path.name}"', log=True)
        
        print(f"✅ Unzipping {UI}...")
        # --- THIS IS THE FIX ---
        # Replacing ipySys with the standard subprocess library
        try:
            subprocess.run(
                ['unzip', '-o', str(zip_path), '-d', str(WEBUI_PATH)],
                check=True, capture_output=True, text=True
            )
            print(f"✅ Cleaning up zip file...")
            zip_path.unlink()
            print(f"✅ {UI} installation complete!")
        except subprocess.CalledProcessError as e:
            print(f"❌ UNZIP FAILED for {UI}:\n{e.stderr}", file=sys.stderr)
            sys.exit(1)
        # --- END OF FIX ---
            
    else:
        print(f"✨ {UI} directory already exists. Skipping installation.")

if __name__ == '__main__':
    main()