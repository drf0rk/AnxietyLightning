# /content/ANXETY/scripts/UIs/ReForge.py (Modified for Debugging)

from Manager import m_download
import json_utils as js
from IPython import get_ipython
from pathlib import Path
import os
import asyncio

CD = os.chdir
ipySys = get_ipython().system

# Constants
UI = 'ReForge'
HOME = Path.home()
WEBUI = HOME / UI
VENV = HOME / 'venv'
SCR_PATH = HOME / 'ANXETY'
SETTINGS_PATH = SCR_PATH / 'settings.json'

ENV_NAME = js.read(SETTINGS_PATH, 'ENVIRONMENT.env_name')
REPO_URL = f"https://huggingface.co/NagisaNao/ANXETY/resolve/main/{UI}.zip"
FORK_REPO = js.read(SETTINGS_PATH, 'ENVIRONMENT.fork')
BRANCH = js.read(SETTINGS_PATH, 'ENVIRONMENT.branch')
EXTS = js.read(SETTINGS_PATH, 'WEBUI.extension_dir')

CD(HOME)

async def _download_file(url, directory, filename):
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, filename)
    if os.path.exists(file_path): os.remove(file_path)
    process = await asyncio.create_subprocess_shell(
        f"curl -sLo {file_path} {url}",
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    await process.communicate()

async def download_files(file_list):
    tasks = []
    for file_info in file_list:
        parts = file_info.split(',')
        url = parts[0].strip()
        directory = parts[1].strip() if len(parts) > 1 else str(WEBUI)
        filename = parts[2].strip() if len(parts) > 2 else os.path.basename(url)
        tasks.append(_download_file(url, directory, filename))
    await asyncio.gather(*tasks)

async def download_configuration():
    url_cfg = f"https://raw.githubusercontent.com/{FORK_REPO}/{BRANCH}/__configs__"
    configs = [
        f"{url_cfg}/{UI}/config.json,{str(WEBUI)}",
        f"{url_cfg}/{UI}/ui-config.json,{str(WEBUI)}",
        f"{url_cfg}/styles.csv,{str(WEBUI)}",
        f"{url_cfg}/user.css,{str(WEBUI)}",
        f"{url_cfg}/card-no-preview.png,{str(WEBUI / 'html')}",
        f"{url_cfg}/notification.mp3,{str(WEBUI)}",
        f"{url_cfg}/gradio-tunneling.py,{str(VENV / 'lib/python3.10/site-packages/gradio_tunneling')},main.py"
    ]
    await download_files(configs)
    
    extensions_list = [
        'https://github.com/anxety-solo/webui_timer timer',
        'https://github.com/anxety-solo/anxety-theme',
        'https://github.com/anxety-solo/sd-civitai-browser-plus Civitai-Browser-Plus',
        'https://github.com/gutris1/sd-image-viewer Image-Viewer',
        'https://github.com/gutris1/sd-image-info Image-Info',
        'https://github.com/gutris1/sd-hub SD-Hub',
        'https://github.com/Bing-su/adetailer',
    ]
    if ENV_NAME == 'Kaggle':
        extensions_list.append('https://github.com/gutris1/sd-encrypt-image Encrypt-Image')

    os.makedirs(EXTS, exist_ok=True)
    CD(EXTS)
    tasks = [asyncio.create_subprocess_shell(f"git clone --depth 1 {command}", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) for command in extensions_list]
    await asyncio.gather(*tasks)

def unpack_webui():
    zip_path = f"{HOME}/{UI}.zip"
    print(f"--- DEBUG: Calling m_download for {REPO_URL} ---")
    m_download(f"{REPO_URL} {HOME} {UI}.zip", log=True)
    
    print(f"--- DEBUG: Unzipping {zip_path} to {WEBUI} ---")
    ipySys(f"unzip -o {zip_path} -d {WEBUI}") # Removed -q for verbose output
    
    print(f"--- DEBUG: Removing {zip_path} ---")
    ipySys(f"rm -rf {zip_path}")
    print("--- DEBUG: unpack_webui finished ---")

## ====================== MAIN CODE ======================
if __name__ == '__main__':
    # --- THIS IS THE FIX ---
    # The `with capture.capture_output():` line has been removed to expose all errors.
    print("--- DEBUG: Starting ReForge UI installer ---")
    unpack_webui()
    asyncio.run(download_configuration())
    print("--- DEBUG: ReForge UI installer finished ---")
    # --- END OF FIX ---