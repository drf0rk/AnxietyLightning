# ~ A1111.py | by ANXETY ~ (Corrected with Self-Aware Pathing)

import os
import sys
from pathlib import Path
import subprocess
import asyncio

# --- Self-aware pathing to find project root and modules ---
try:
    # From .../scripts/UIs/ the root is 2 levels up
    ANXETY_ROOT = Path(__file__).resolve().parents[2]
except NameError:
    ANXETY_ROOT = Path.cwd()
# Add the modules directory to the Python path
if str(ANXETY_ROOT / 'modules') not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT / 'modules'))
# ---

from Manager import m_download
import json_utils as js
from IPython import get_ipython

CD = os.chdir
ipySys = get_ipython().system

# Constants
UI = 'A1111'
HOME = Path.home()
WEBUI = HOME / UI
SETTINGS_PATH = ANXETY_ROOT / 'settings.json'
REPO_URL = f"https://huggingface.co/NagisaNao/ANXETY/resolve/main/{UI}.zip"

def unpack_webui():
    zip_path = HOME / f"{UI}.zip"
    # Using the original, correct workflow
    m_download(f'"{REPO_URL}" "{HOME}" "{zip_path.name}"', log=True)
    ipySys(f"unzip -o {zip_path} -d {WEBUI}") # Removed -q for verbose output
    ipySys(f"rm -rf {zip_path}")

## ====================== MAIN CODE ======================
if __name__ == '__main__':
    unpack_webui()
    # Any additional async config downloads would go here