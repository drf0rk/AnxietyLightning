# /content/ANXETY/scripts/UIs/ReForge.py (Definitive Final Version)

import os
import sys
from pathlib import Path
import subprocess

# --- Self-aware pathing to find project root and modules ---
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[2]
except NameError:
    ANXETY_ROOT = Path.cwd()
if str(ANXETY_ROOT) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT))
# ---

from modules.Manager import m_download
from IPython import get_ipython

ipySys = get_ipython().system
HOME = Path.home()
UI = 'ReForge'
WEBUI_PATH = HOME / UI
REPO_URL = f"https://huggingface.co/NagisaNao/ANXETY/resolve/main/{UI}.zip"

def main():
    if not WEBUI_PATH.exists():
        print(f"✅ Downloading and unpacking {UI} from Hugging Face...")
        zip_path = HOME / f"{UI}.zip"
        
        # Command format for m_download is "URL" "DESTINATION_DIR" "FILENAME"
        m_download(f'"{REPO_URL}" "{HOME}" "{zip_path.name}"', log=True)
        
        print(f"✅ Unzipping {UI}...")
        # Use -d to specify extraction directory, -o to overwrite without asking
        ipySys(f"unzip -o {zip_path} -d {WEBUI_PATH}")
        
        print(f"✅ Cleaning up zip file...")
        zip_path.unlink()
        
        print(f"✅ {UI} installation complete!")
    else:
        print(f"✨ {UI} directory already exists. Skipping installation.")

if __name__ == '__main__':
    main()