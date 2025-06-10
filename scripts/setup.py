# /content/ANXETY/scripts/setup.py (Definitive Final Version for Notebooks)

import os
import sys
import json
import time
import argparse
from pathlib import Path
import asyncio
import aiohttp
from tqdm.auto import tqdm
import nest_asyncio

# Apply the patch to allow nested asyncio loops
nest_asyncio.apply()

# --- Platform Detection and Path Setup ---
def detect_platform():
    if 'google.colab' in sys.modules: return 'colab'
    if os.path.exists('/kaggle'): return 'kaggle'
    if os.environ.get('LIGHTNING_AI') or os.path.exists('/teamspace'): return 'lightning'
    return 'local'

def get_home_path(platform):
    if platform == 'lightning':
        base_path = Path('/teamspace/studios/this_studio')
        return base_path if base_path.exists() else Path.home() / 'workspace'
    if platform == 'colab': return Path('/content')
    if platform == 'kaggle': return Path('/kaggle/working')
    return Path.cwd()

CURRENT_PLATFORM = detect_platform()
HOME = get_home_path(CURRENT_PLATFORM)
ANXETY_ROOT = HOME / 'ANXETY'
SETTINGS_PATH = ANXETY_ROOT / 'settings.json'
ANXETY_ROOT.mkdir(parents=True, exist_ok=True)

# --- JSON Utilities ---
def save_json(filepath, data):
    existing_data = {}
    if filepath.exists():
        try:
            with open(filepath, 'r') as f: existing_data = json.load(f)
        except json.JSONDecodeError: pass
    for key, value in data.items():
        if key in existing_data and isinstance(existing_data[key], dict) and isinstance(value, dict):
            existing_data[key].update(value)
        else:
            existing_data[key] = value
    with open(filepath, 'w') as f: json.dump(existing_data, f, indent=4)

def read_json(filepath, key, default=None):
    if not filepath.exists(): return default
    try:
        with open(filepath, 'r') as f: data = json.load(f)
        for k in key.split('.'): data = data[k]
        return data
    except (json.JSONDecodeError, KeyError): return default

# --- Main Logic ---
def create_environment_data():
    platform_name_map = {'colab': 'Google Colab', 'kaggle': 'Kaggle', 'lightning': 'Lightning AI', 'local': 'Local'}
    return {
        'ENVIRONMENT': {
            'env_name': platform_name_map.get(CURRENT_PLATFORM, 'Unknown'),
            'home_path': str(HOME),
            'scr_path': str(ANXETY_ROOT),
            'venv_path': str(HOME / 'venv'),
            'start_timer': read_json(SETTINGS_PATH, 'ENVIRONMENT.start_timer', int(time.time())),
        }
    }

async def download_file(session, url, path):
    try:
        async with session.get(url) as resp:
            resp.raise_for_status()
            content = await resp.read()
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
    except Exception as e:
        print(f"Failed to download {url}: {e}", file=sys.stderr)

async def download_all_files(fork_repo, branch):
    base_url = f"https://raw.githubusercontent.com/{fork_repo}/{branch}"
    # Expanded list to ensure all modules and UI scripts are present
    files_to_download = {
        'modules/Manager.py': 'modules/Manager.py', 'modules/CivitaiAPI.py': 'modules/CivitaiAPI.py',
        'modules/json_utils.py': 'modules/json_utils.py', 'modules/webui_utils.py': 'modules/webui_utils.py',
        'modules/widget_factory.py': 'modules/widget_factory.py', 'modules/__season.py': 'modules/__season.py',
        'scripts/UIs/A1111.py': 'scripts/UIs/A1111.py', 'scripts/UIs/Forge.py': 'scripts/UIs/Forge.py',
        'scripts/UIs/ReForge.py': 'scripts/UIs/ReForge.py', 'scripts/UIs/ComfyUI.py': 'scripts/UIs/ComfyUI.py',
        'scripts/UIs/SD-UX.py': 'scripts/UIs/SD-UX.py',
        'scripts/en/widgets-en.py': 'scripts/en/widgets-en.py', 'scripts/en/downloading-en.py': 'scripts/en/downloading-en.py',
        'scripts/launch.py': 'scripts/launch.py', 'scripts/_models-data.py': 'scripts/_models-data.py',
        'scripts/_xl-models-data.py': 'scripts/_xl-models-data.py', 'scripts/_loras-data.py': 'scripts/_loras-data.py',
    }
    
    async with aiohttp.ClientSession() as session:
        tasks = [download_file(session, f"{base_url}/{remote}", ANXETY_ROOT / local) for remote, local in files_to_download.items()]
        for f in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Deploying scripts"): await f

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fork', type=str, default='drf0rk/AnxietyLightning', help='Project fork')
    parser.add_argument('-b', '--branch', type=str, default='main', help='Branch to download from')
    parser.add_argument('--lang', type=str, default='en')
    args, _ = parser.parse_known_args()

    print("🚀 Initializing environment...")
    
    env_data = create_environment_data()
    env_data['ENVIRONMENT']['fork'] = args.fork
    env_data['ENVIRONMENT']['branch'] = args.branch
    save_json(SETTINGS_PATH, env_data)
    
    # --- THIS IS THE FIX ---
    # We get the existing loop from the notebook and run our async function in it.
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_all_files(args.fork, args.branch))
    # --- END OF FIX ---

    print("✅ Environment setup complete.")
    print(f"✔️ Project Root: {HOME}")
    print(f"✔️ ANXETY scripts installed in: {ANXETY_ROOT}")

if __name__ == '__main__':
    main()