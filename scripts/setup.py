# ~ setup.py | by ANXETY ~ (Multi-Platform Restoration)

import sys
from pathlib import Path
import os

# VERY EARLY SYS.PATH MODIFICATION FOR CRITICAL IMPORTS
_HOME_EARLY = Path.home()
_ANXETY_PATH_EARLY = _HOME_EARLY / 'ANXETY'
_MODULES_PATH_EARLY = _ANXETY_PATH_EARLY / 'modules'
_SCRIPTS_PATH_EARLY = _ANXETY_PATH_EARLY / 'scripts'

_MODULES_PATH_EARLY.mkdir(parents=True, exist_ok=True)
_SCRIPTS_PATH_EARLY.mkdir(parents=True, exist_ok=True)

if str(_MODULES_PATH_EARLY) not in sys.path:
    sys.path.insert(0, str(_MODULES_PATH_EARLY))
if str(_SCRIPTS_PATH_EARLY) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_PATH_EARLY))
# END VERY EARLY SYS.PATH MODIFICATION

from IPython.display import display, HTML, clear_output
from urllib.parse import urljoin
from tqdm import tqdm
import nest_asyncio
import importlib
import argparse
import asyncio
import aiohttp
import time
import json

nest_asyncio.apply()

# ===================== DYNAMIC PLATFORM DETECTION =====================

def detect_platform():
    """Detects the current runtime environment (Colab, Kaggle, Lightning, or Local)."""
    try:
        import google.colab
        return 'colab'
    except ImportError:
        pass

    if os.path.exists('/kaggle'):
        return 'kaggle'

    if (
        os.environ.get('LIGHTNING_CLOUD_PROJECT_ID') or
        os.environ.get('LIGHTNING_AI') or
        os.path.exists('/teamspace')
    ):
        return 'lightning'

    return 'local'

CURRENT_PLATFORM = detect_platform()
print(f"✅ Platform detected: {CURRENT_PLATFORM}")

# ===================== DYNAMIC PATH SETUP =====================

def get_home_path(platform):
    """Returns the appropriate home directory based on the detected platform."""
    if platform == 'lightning':
        # Lightning AI uses a specific workspace directory
        base_path = Path('/teamspace/studios/this_studio')
        if not base_path.exists():
            base_path = Path.home() / 'workspace'
        base_path.mkdir(parents=True, exist_ok=True)
        return base_path
    elif platform == 'colab':
        return Path('/content')
    elif platform == 'kaggle':
        return Path('/kaggle/working')
    else: # local
        return Path.cwd()

HOME = get_home_path(CURRENT_PLATFORM)
SCR_PATH = HOME / 'ANXETY'
SETTINGS_PATH = SCR_PATH / 'settings.json'

# ===================== UTILITIES =====================

def key_exists(filepath, key=None, value=None):
    if not filepath.exists(): return False
    try:
        with open(filepath, 'r') as f: data = json.load(f)
    except json.JSONDecodeError: return False
    if key:
        keys = key.split('.')
        for k in keys:
            if isinstance(data, dict) and k in data: data = data[k]
            else: return False
        return (data == value) if value is not None else True
    return False

def save_environment_to_json(settings_path, data):
    existing_data = {}
    if settings_path.exists():
        try:
            with open(settings_path, 'r') as f: existing_data = json.load(f)
        except json.JSONDecodeError: existing_data = {}
    existing_data.update(data)
    with open(settings_path, 'w') as f: json.dump(existing_data, f, indent=4)

def get_start_timer():
    if SETTINGS_PATH.exists():
        try:
            with open(SETTINGS_PATH, 'r') as f:
                settings = json.load(f)
                return settings.get('ENVIRONMENT', {}).get('start_timer', int(time.time() - 5))
        except json.JSONDecodeError: return int(time.time() - 5)
    return int(time.time() - 5)

# ======================= MODULES =======================

def clear_module_cache(modules_folder):
    for module_name in list(sys.modules.keys()):
        module = sys.modules[module_name]
        if hasattr(module, '__file__') and module.__file__ and module.__file__.startswith(str(modules_folder)):
            del sys.modules[module_name]
    importlib.invalidate_caches()

def setup_module_folder(scr_folder):
    clear_module_cache(scr_folder)
    modules_folder = scr_folder / 'modules'
    modules_folder.mkdir(parents=True, exist_ok=True)
    if str(modules_folder) not in sys.path:
        sys.path.append(str(modules_folder))

# ===================== ENVIRONMENT SETUP =====================

def get_fork_info(fork_arg):
    if not fork_arg: return 'anxety-solo', 'sdAIgen'
    parts = fork_arg.split('/', 1)
    return parts[0], (parts[1] if len(parts) > 1 else 'sdAIgen')

def create_environment_data(platform, scr_folder, lang, fork_user, fork_repo, branch):
    platform_name_map = {
        'colab': 'Google Colab',
        'kaggle': 'Kaggle',
        'lightning': 'Lightning AI',
        'local': 'Local'
    }
    env_name = platform_name_map.get(platform, 'Unknown')
    
    return {
        'ENVIRONMENT': {
            'lang': lang,
            'fork': f"{fork_user}/{fork_repo}",
            'branch': branch,
            'env_name': env_name,
            'install_deps': key_exists(SETTINGS_PATH, 'ENVIRONMENT.install_deps', True),
            'home_path': str(HOME),
            'venv_path': str(HOME / 'venv'),
            'scr_path': str(scr_folder),
            'start_timer': get_start_timer(),
            'public_ip': ''
        }
    }

# ======================= DOWNLOAD LOGIC =====================

def generate_file_list(structure, base_url, base_path):
    def walk(struct, path_parts):
        items = []
        for key, value in struct.items():
            current_path = [*path_parts, key] if key else path_parts
            if isinstance(value, dict): items.extend(walk(value, current_path))
            else:
                url_path = '/'.join(current_path)
                for file in value:
                    url = f"{base_url}/{url_path}/{file}" if url_path else f"{base_url}/{file}"
                    file_path = base_path / '/'.join(current_path) / file
                    items.append((url, file_path))
        return items
    return walk(structure, [])

async def download_file(session, url, path):
    try:
        async with session.get(url) as resp:
            resp.raise_for_status()
            content = await resp.read()
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
            return (True, url, path, None)
    except aiohttp.ClientResponseError as e:
        return (False, url, path, f"HTTP error {e.status}: {e.message}")
    except Exception as e:
        return (False, url, path, f"Error: {str(e)}")

async def download_files_async(scr_path, lang, fork_user, fork_repo, branch, log_errors):
    files_structure = {
        'CSS': ['main-widgets.css', 'download-result.css', 'auto-cleaner.css'],
        'JS': ['main-widgets.js'],
        'modules': ['json_utils.py', 'webui_utils.py', 'widget_factory.py',
                   'TunnelHub.py', 'CivitaiAPI.py', 'Manager.py', '__season.py'],
        'scripts': {
            'UIs': ['A1111.py', 'ComfyUI.py', 'Forge.py', 'Classic.py', 'ReForge.py', 'SD-UX.py'],
            lang: [f"widgets-{lang}.py", f"downloading-{lang}.py"],
            '': ['launch.py', 'auto-cleaner.py', 'download-result.py',
                 '_models-data.py', '_xl-models-data.py', '_loras-data.py']
        }
    }
    base_url = f"https://raw.githubusercontent.com/{fork_user}/{fork_repo}/{branch}"
    file_list = generate_file_list(files_structure, base_url, scr_path)
    async with aiohttp.ClientSession() as session:
        tasks = [download_file(session, url, path) for url, path in file_list]
        errors = []
        futures = asyncio.as_completed(tasks)
        for future in tqdm(futures, total=len(tasks), desc="Downloading files", unit="file"):
            result = await future
            if not result[0]: errors.append(result[1:])
        clear_output()
        if log_errors and errors:
            print("\nErrors occurred during download:")
            for url, path, error in errors: print(f"URL: {url}\nPath: {path}\nError: {error}\n")

# ===================== MAIN EXECUTION =====================

async def main_async(args=None):
    parser = argparse.ArgumentParser(description='ANXETY Download Manager')
    parser.add_argument('-l', '--lang', type=str, default='en', help='Language to be used')
    parser.add_argument('-b', '--branch', type=str, default='main', help='Branch to download from')
    parser.add_argument('-f', '--fork', type=str, default=None, help='Project fork (user/repo)')
    parser.add_argument('-s', '--skip-download', action='store_true', help='Skip downloading files')
    parser.add_argument('-L', '--log', action='store_true', help='Log download errors')
    args, _ = parser.parse_known_args(args)

    user, repo = get_fork_info(args.fork)

    if not args.skip_download:
        await download_files_async(SCR_PATH, args.lang, user, repo, args.branch, args.log)

    setup_module_folder(SCR_PATH)
    
    # This must come after setup_module_folder to ensure __season is importable
    from __season import display_info

    # Save environment data to settings.json
    env_data = create_environment_data(CURRENT_PLATFORM, SCR_PATH, args.lang, user, repo, args.branch)
    save_environment_to_json(SETTINGS_PATH, env_data)

    display_info(
        env=env_data['ENVIRONMENT']['env_name'],
        scr_folder=str(SCR_PATH),
        branch=args.branch,
        lang=args.lang,
        fork=args.fork
    )

if __name__ == '__main__':
    asyncio.run(main_async())