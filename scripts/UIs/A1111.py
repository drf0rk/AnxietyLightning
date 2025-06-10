# /content/ANXETY/scripts/UIs/A1111.py (Definitive Final Version)

import os
import sys
from pathlib import Path
import subprocess

# --- Self-aware pathing ---
try: ANXETY_ROOT = Path(__file__).resolve().parents[2]
except NameError: ANXETY_ROOT = Path.cwd() / 'ANXETY'
if str(ANXETY_ROOT) not in sys.path: sys.path.insert(0, str(ANXETY_ROOT))
if str(ANXETY_ROOT / 'modules') not in sys.path: sys.path.insert(0, str(ANXETY_ROOT / 'modules'))
# ---

from Manager import m_download
import json_utils as js

SETTINGS_PATH = ANXETY_ROOT / 'settings.json'
HOME = Path(js.read(SETTINGS_PATH, 'ENVIRONMENT.home_path', str(Path.home())))

UI = 'A1111'
WEBUI_PATH = HOME / UI
REPO_URL = f"https://huggingface.co/NagisaNao/ANXETY/resolve/main/{UI}.zip"

def main():
    if not WEBUI_PATH.exists():
        print(f"✅ Downloading and unpacking {UI} to {WEBUI_PATH}...")
        zip_path = HOME / f"{UI}.zip"
        m_download(f'"{REPO_URL}" "{HOME}" "{zip_path.name}"', log=True)
        if not zip_path.exists():
            print(f"❌ DOWNLOAD FAILED for {UI}", file=sys.stderr); sys.exit(1)
        try:
            WEBUI_PATH.mkdir(parents=True, exist_ok=True)
            subprocess.run(['unzip', '-o', str(zip_path), '-d', str(WEBUI_PATH)], check=True, capture_output=True)
            zip_path.unlink()
            print(f"✅ {UI} installation complete!")
        except Exception as e:
            print(f"❌ UNZIP FAILED for {UI}: {e}", file=sys.stderr); sys.exit(1)
    else:
        print(f"✨ {UI} directory already exists. Skipping.")

if __name__ == '__main__':
    main()