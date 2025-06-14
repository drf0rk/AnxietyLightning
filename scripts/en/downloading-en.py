# /content/ANXETY/scripts/en/downloading-en.py

import os
import sys
from pathlib import Path
import json
import time

# Add project root to path if not already there
ANXETY_ROOT = Path(os.environ.get("ANXETY_ROOT", "/content/ANXETY"))
if str(ANXETY_ROOT) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT))

try:
    from modules import json_utils as js
    from modules import logging_utils as m
    from modules import utils as u
    from modules import download_utils as d # Assuming download functions are here
except ImportError as e:
    print(f"❌ CRITICAL: Failed to import core modules in downloading-en.py. Error: {e}")
    sys.exit(1)

# --- Configuration ---
HOME_DIR = Path(os.environ.get("HOME_DIR", "/content"))
SETTINGS_PATH = ANXETY_ROOT / "settings.json"
LOG_DIR = ANXETY_ROOT / "logs"
VENV_DIR = HOME_DIR / "venv"
TEMP_DIR = HOME_DIR / "temp"
TEMP_DIR.mkdir(exist_ok=True, parents=True)

m.configure_logging(LOG_DIR / "download.log")

# --- Data Loading (Models, VAEs, etc.) ---
try:
    # Assume data files are loaded here or imported
    sd15_data = u.load_data_file(ANXETY_ROOT / 'scripts/_models-data.py')
    sdxl_data = u.load_data_file(ANXETY_ROOT / 'scripts/_xl-models-data.py')
    loras_data_full = u.load_data_file(ANXETY_ROOT / 'scripts/_loras-data.py')
    # ... Extract specific dictionaries ...
except Exception as e:
    m.log("error", f"FATAL: Failed to load asset data files. Error: {e}")
    sys.exit(1)

# --- Load Settings ---
m.log("info", "--- 🚀 Stage D1: Loading Download Configuration ---")
try:
    settings = js.read(str(SETTINGS_PATH))
    WIDGETS = settings.get('WIDGETS', {})
    WEBUI_NAME = WIDGETS.get('change_webui', 'ReForge') # Default to ReForge if missing
    # ... Load other settings like selected models, is_sdxl, etc. ...
    m.log("info", f"Target WebUI for installation: {WEBUI_NAME}")
except Exception as e:
    m.log("error", f"FATAL: Failed to read or parse {SETTINGS_PATH}. Error: {e}")
    sys.exit(1)

# --- Hardcoded URLs (as seen in previous debug sessions) ---
# These should ideally be in a config file, but keeping them here as per original structure
VENV_URLS = {
    "default": "https://huggingface.co/NagisaNao/ANXETY/resolve/main/venv.tar.lz4"
}
WEBUI_URLS = {
    "ReForge": "https://huggingface.co/NagisaNao/ANXETY/resolve/main/ReForge.zip",
    "Forge": "https://huggingface.co/NagisaNao/ANXETY/resolve/main/Forge.zip",
    "A1111": "https://huggingface.co/NagisaNao/ANXETY/resolve/main/A1111.zip",
    "ComfyUI": "https://huggingface.co/NagisaNao/ANXETY/resolve/main/ComfyUI.zip",
    "Classic": "https://huggingface.co/NagisaNao/ANXETY/resolve/main/Classic.zip",
    "SD-UX": "https://huggingface.co/NagisaNao/ANXETY/resolve/main/SD-UX.zip",
}

# --- VENV Installation ---
def install_venv():
    m.log("info", "--- 🚀 Stage D2: Installing VENV ---")
    venv_url = VENV_URLS.get("default")
    archive_path = TEMP_DIR / "venv.tar.lz4"

    if VENV_DIR.exists() and (VENV_DIR / "bin/python").exists():
        m.log("info", f"VENV already exists at {VENV_DIR}. Skipping installation.")
        return

    m.log("info", f"Downloading VENV from {venv_url}")
    try:
        # Use the robust huggingface-hub downloader logic from download_utils
        d.download_file(venv_url, str(archive_path))
        m.log("success", f"VENV archive downloaded to {archive_path}")
    except Exception as e:
        m.log("error", f"FATAL: Failed to download VENV. Error: {e}")
        sys.exit(1)

    m.log("info", f"Extracting VENV archive to {HOME_DIR} (This may take a while...)")
    try:
        # Use the robust extraction logic from utils (handles lz4)
        u.extract(str(archive_path), str(HOME_DIR))
        if (VENV_DIR / "bin/python").exists():
             m.log("success", f"✅ VENV successfully extracted and verified at {VENV_DIR}")
        else:
             m.log("error", f"FATAL: VENV extraction finished but {VENV_DIR / 'bin/python'} is missing.")
             sys.exit(1)
    except Exception as e:
        m.log("error", f"FATAL: Failed to extract VENV. Error: {e}")
        sys.exit(1)
    finally:
        u.safe_remove(archive_path)

# --- WebUI Installation ---
def install_webui(webui_name):
    m.log("info", f"--- 🚀 Stage D3: Installing WebUI ({webui_name}) ---")
    webui_url = WEBUI_URLS.get(webui_name)
    if not webui_url:
        m.log("error", f"FATAL: No URL found for WebUI '{webui_name}'. Cannot install.")
        sys.exit(1)

    archive_name = f"{webui_name}.zip"
    archive_path = TEMP_DIR / archive_name

    # Note: We don't check if it exists here, as the user might want to reinstall/update
    m.log("info", f"Downloading {webui_name} from {webui_url}")
    try:
        d.download_file(webui_url, str(archive_path))
        m.log("success", f"WebUI archive downloaded to {archive_path}")
    except Exception as e:
        m.log("error", f"FATAL: Failed to download WebUI '{webui_name}'. Error: {e}")
        sys.exit(1)

    m.log("info", f"Extracting {archive_name} to {HOME_DIR}")
    m.log("warning", f"Note: Files will be extracted directly into {HOME_DIR}. If the archive contains a top-level folder, it will be created. Otherwise, files will land in {HOME_DIR}.")
    try:
        # Use the robust extraction logic from utils
        u.extract(str(archive_path), str(HOME_DIR))
        m.log("success", f"✅ WebUI '{webui_name}' extracted to {HOME_DIR}.")
        m.log("info", "The launcher script will determine the final working directory.")
    except Exception as e:
        m.log("error", f"FATAL: Failed to extract WebUI '{webui_name}'. Error: {e}")
        sys.exit(1)
    finally:
        u.safe_remove(archive_path)

# --- Model/Asset Downloads ---
def download_assets():
    m.log("info", "--- 🚀 Stage D4: Downloading Selected Assets ---")
    # ... (Keep existing logic for downloading models, LoRAs, etc.) ...
    # Add enhanced logging here too, specifying exact download paths
    m.log("info", "Asset download phase complete.")

# --- Main Execution ---
if __name__ == "__main__":
    m.log("info", "=== Downloading and Environment Setup Started ===")
    start_time = time.time()

    install_venv()
    install_webui(WEBUI_NAME)
    download_assets() # Placeholder for actual asset download logic

    end_time = time.time()
    m.log("success", f"✅✅✅ --- Environment Setup Complete --- ✅✅✅")
    m.log("info", f"Total setup time: {end_time - start_time:.2f} seconds")