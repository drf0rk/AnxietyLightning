# ~ ReForge.py | by ANXETY ~ (Corrected with Centralized Pathing)

import os
import sys
from pathlib import Path
import asyncio
import subprocess

# --- Add modules to path to import utils ---
# This robustly finds the ANXETY folder regardless of the platform
try:
    # On Colab, home is /root, but the files are in /content.
    project_home = Path('/content') if os.path.exists('/content') else Path.home()
    anxety_path = project_home / 'ANXETY'
    if not anxety_path.exists(): # Fallback for Lightning AI or other structures
        anxety_path = Path.cwd() / 'ANXETY'
    
    modules_path = anxety_path / 'modules'
    if str(modules_path) not in sys.path:
        sys.path.insert(0, str(modules_path))

    import json_utils as js
    from Manager import m_download
except ImportError as e:
    print(f"FATAL ERROR: Could not import core modules in ReForge.py. Pathing issue: {e}")
    sys.exit(1)


# --- Get All Paths from the Single Source of Truth: settings.json ---
SETTINGS_PATH = anxety_path / 'settings.json'
settings = js.read(SETTINGS_PATH)
env_settings = settings.get('ENVIRONMENT', {})
webui_settings = settings.get('WEBUI', {})

# Constants now defined from the central settings file
UI = 'ReForge'
HOME = Path(env_settings.get('home_path'))
WEBUI = HOME / UI # Construct the correct path
VENV = Path(env_settings.get('venv_path'))
FORK_REPO = env_settings.get('fork')
BRANCH = env_settings.get('branch')
EXTS = Path(webui_settings.get('extension_dir'))

CD = os.chdir
ipySys = get_ipython().system

# --- The rest of the script now uses the correct paths ---

async def _download_file(url, directory, filename):
    """Downloads a single file."""
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, filename)
    if os.path.exists(file_path): os.remove(file_path)
    process = await asyncio.create_subprocess_shell(
        f"curl -sLo \"{file_path}\" \"{url}\"",
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    await process.communicate()

async def download_files(file_list):
    """Downloads multiple files asynchronously."""
    tasks = []
    for file_info in file_list:
        parts = file_info.split(',')
        url = parts[0].strip()
        directory = parts[1].strip() if len(parts) > 1 else str(WEBUI)
        filename = parts[2].strip() if len(parts) > 2 else os.path.basename(url)
        tasks.append(_download_file(url, directory, filename))
    await asyncio.gather(*tasks)

async def download_configuration():
    """Downloads configuration files and clones extensions."""
    url_cfg = f"https://raw.githubusercontent.com/{FORK_REPO}/{BRANCH}/__configs__"
    # Corrected python version to be dynamic
    py_version = f"python{sys.version_info.major}.{sys.version_info.minor}"
    configs = [
        f"{url_cfg}/{UI}/config.json",
        f"{url_cfg}/{UI}/ui-config.json",
        f"{url_cfg}/styles.csv",
        f"{url_cfg}/user.css",
        f"{url_cfg}/card-no-preview.png,{str(WEBUI / 'html')}",
        f"{url_cfg}/notification.mp3",
        f"{url_cfg}/gradio-tunneling.py,{str(VENV / 'lib' / py_version / 'site-packages' / 'gradio_client')},tunnel.py"
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
        'https://github.com/Haoming02/sd-webui-mosaic-outpaint',
        'https://github.com/continue-revolution/sd-webui-segment-anything',
        'https://github.com/kainatquaderee/sd-webui-reactor-Nsfw_freedom',
        'https://github.com/a2569875/lora-prompt-tool',
        'https://github.com/Uminosachi/sd-webui-inpaint-anything',
        'https://github.com/redmercy69/sd-webui-stripper',
        'https://github.com/diffus-me/sd-webui-facefusion',
        'https://github.com/glucauze/sd-webui-faceswaplab',
        'https://github.com/IntellectzProductions/sd-webui-faceswap',
        'https://github.com/yownas/sd-webui-faceswapper',
        'https://github.com/leeguandong/sd_webui_outpainting',
        'https://github.com/thoraxe69/sd-webui-roop',
    ]
    
    os.makedirs(EXTS, exist_ok=True)
    CD(EXTS)
    tasks = [asyncio.create_subprocess_shell(f"git clone --depth 1 {cmd}", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) for cmd in extensions_list]
    await asyncio.gather(*tasks)

def unpack_webui():
    """Unpacks the WebUI zip file and cleans up model-related directories."""
    REPO_URL = f"https://huggingface.co/NagisaNao/ANXETY/resolve/main/{UI}.zip"
    zip_path = f"{HOME}/{UI}.zip"
    m_download(f"\"{REPO_URL}\" \"{HOME}\" \"{UI}.zip\"")
    ipySys(f"unzip -q -o \"{zip_path}\" -d \"{WEBUI}\"")
    ipySys(f"rm -rf \"{zip_path}\"")
    
    model_dirs_to_clean = ['models', 'VAE', 'Lora', 'embeddings', 'ControlNet']
    for d_name in model_dirs_to_clean:
        d_path = WEBUI / d_name
        if d_path.exists() and d_path.is_dir():
            print(f"   Deleting stub directory: {d_path}")
            shutil.rmtree(d_path)

if __name__ == '__main__':
    from IPython.utils import capture
    with capture.capture_output():
        unpack_webui()
        asyncio.run(download_configuration())