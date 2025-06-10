# ~ ComfyUI.py | by ANXETY ~

from Manager import m_download, m_clone    # Every Download | Clone
import json_utils as js                    # JSON

from IPython.display import clear_output
from IPython.utils import capture
from IPython import get_ipython
from pathlib import Path
import subprocess
import asyncio
import os
import shutil # Import shutil for rmtree

CD = os.chdir
ipySys = get_ipython().system

# Constants
UI = 'ComfyUI'

HOME = Path.home()
VENV = HOME / 'venv'
WEBUI = HOME / UI
SCR_PATH = HOME / 'ANXETY'
SETTINGS_PATH = SCR_PATH / 'settings.json'

ENV_NAME = js.read(SETTINGS_PATH, 'ENVIRONMENT.env_name')

REPO_URL = f"https://huggingface.co/NagisaNao/ANXETY/resolve/main/{UI}.zip"
FORK_REPO = js.read(SETTINGS_PATH, 'ENVIRONMENT.fork')
BRANCH = js.read(SETTINGS_PATH, 'ENVIRONMENT.branch')
EXTS = js.read(SETTINGS_PATH, 'WEBUI.extension_dir')

CD(HOME)


## ================== WEB UI OPERATIONS ==================

async def _download_file(url, directory, filename):
    """Downloads a single file."""
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, filename)
    process = await asyncio.create_subprocess_shell(
        f"curl -sLo {file_path} {url}",
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    await process.communicate()

async def download_files(file_list):
    """Downloads multiple files asynchronously."""
    tasks = []
    for file_info in file_list:
        parts = file_info.split(',')
        url = parts[0].strip()
        directory = parts[1].strip() if len(parts) > 1 else WEBUI   # Default Save Path
        filename = parts[2].strip() if len(parts) > 2 else os.path.basename(url)
        tasks.append(_download_file(url, directory, filename))
    await asyncio.gather(*tasks)

async def download_configuration():
    """Downloads configuration files and clones extensions."""
    ## FILES
    url_cfg = f"https://raw.githubusercontent.com/{FORK_REPO}/{BRANCH}/__configs__"
    files = [
        # settings
        f"{url_cfg}/{UI}/install-deps.py",
        f"{url_cfg}/{UI}/comfy.settings.json, {WEBUI}/user/default",                         # ComfyUI settings
        f"{url_cfg}/{UI}/Comfy-Manager/config.ini, {WEBUI}/user/default/ComfyUI-Manager",    # ComfyUI-Manager settings
        # workflows
        f"{url_cfg}/{UI}/workflows/anxety-workflow.json, {WEBUI}/user/default/workflows",
        # other | tunneling
        f"{url_cfg}/gradio-tunneling.py, {VENV}/lib/python3.10/site-packages/gradio_tunneling, main.py"  # Replace py-Script
    ]
    await download_files(files)

    ## REPOS
    extensions_list = [
        'https://github.com/Fannovel16/comfyui_controlnet_aux',
        'https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet',
        'https://github.com/hayden-fr/ComfyUI-Model-Manager',
        'https://github.com/jags111/efficiency-nodes-comfyui',
        'https://github.com/ltdrdata/ComfyUI-Impact-Pack',
        'https://github.com/ltdrdata/ComfyUI-Impact-Subpack',
        'https://github.com/ltdrdata/ComfyUI-Manager',
        'https://github.com/pythongosssss/ComfyUI-Custom-Scripts',
        'https://github.com/pythongosssss/ComfyUI-WD14-Tagger',
        'https://github.com/ssitu/ComfyUI_UltimateSDUpscale',
        'https://github.com/WASasquatch/was-node-suite-comfyui'
    ]
    os.makedirs(EXTS, exist_ok=True)
    CD(EXTS)

    tasks = []
    for command in extensions_list:
        tasks.append(asyncio.create_subprocess_shell(
            f"git clone --depth 1 --recursive {command}",
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        ))

    await asyncio.gather(*tasks)

def unpack_webui():
    """Unpacks the WebUI zip file and cleans up model-related directories."""
    zip_path = f"{HOME}/{UI}.zip"
    m_download(f"{REPO_URL} {HOME} {UI}.zip")
    ipySys(f"unzip -q -o {zip_path} -d {WEBUI}")
    ipySys(f"rm -rf {zip_path}")
    
    # --- START OF MODIFICATION ---
    # Define model-related directories that should NOT be in the WebUI folder
    # as they are handled by the shared model base for ComfyUI.
    model_dirs_to_clean = [
        WEBUI / 'models', # Sometimes present, needs to be removed
        WEBUI / 'checkpoints',
        WEBUI / 'vae',
        WEBUI / 'loras',
        # 'custom_nodes' is typically handled by extensions cloning directly to EXTS (WEBUI/custom_nodes)
        # So it's generally safe to remove if found here, as proper nodes are in EXTS.
        WEBUI / 'custom_nodes', 
        WEBUI / 'embeddings', # ComfyUI might unpack this as 'embeddings'
        WEBUI / 'controlnet', # ComfyUI might unpack this as 'controlnet'
        WEBUI / 'upscale_models' # For ComfyUI
    ]

    print(f"🧹 Cleaning up unzipped model-related directories within {UI}...")
    for d in model_dirs_to_clean:
        if d.exists() and d.is_dir():
            print(f"   Deleting: {d}")
            try:
                shutil.rmtree(d)
            except OSError as e:
                print(f"   Error deleting {d}: {e}")
    # --- END OF MODIFICATION ---

## ====================== MAIN CODE ======================
if __name__ == '__main__':
    with capture.capture_output():
        unpack_webui()
        asyncio.run(download_configuration())

