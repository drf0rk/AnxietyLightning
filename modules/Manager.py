# /content/ANXETY/modules/Manager.py (vRobust - HF Hub Downloader)

import os
import sys
from pathlib import Path
from urllib.parse import urlparse, unquote
import subprocess
import requests
import zipfile
import shlex
import re
import json
import time
import shutil
from huggingface_hub import hf_hub_download
from huggingface_hub.utils import GatedRepoError, HfHubHTTPError

# --- Self-aware pathing ---
try:
    ANXETY_ROOT_MANAGER = Path(__file__).resolve().parents[1]
except NameError:
    ANXETY_ROOT_MANAGER = Path('/content/ANXETY')

if str(ANXETY_ROOT_MANAGER) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT_MANAGER))
# ---

from modules.CivitaiAPI import CivitAiAPI
import modules.json_utils as js

SETTINGS_PATH_IN_MANAGER = ANXETY_ROOT_MANAGER / 'settings.json'

def log_manager(level, message, data=None):
    log_entry = {"type": "log", "level": level, "message": message, "data": data or {}}
    print(json.dumps(log_entry), flush=True)

def get_tokens_manager():
    cai_token = js.read(SETTINGS_PATH_IN_MANAGER, 'WIDGETS.civitai_token', '65b66176dcf284b266579de57fbdc024')
    hf_token = js.read(SETTINGS_PATH_IN_MANAGER, 'WIDGETS.huggingface_token', '')
    return cai_token, hf_token

def handle_errors_manager(func):
    def wrapper(*args, **kwargs):
        try: return func(*args, **kwargs)
        except Exception as e:
            log_manager('error', f"Manager Error in {func.__name__}: {e}", data={'args': args, 'kwargs': kwargs})
            return False
    return wrapper

def parse_hf_url(url: str):
    """Parses a Hugging Face URL to extract repo_id and filename."""
    parsed_url = urlparse(url)
    if not parsed_url.netloc == 'huggingface.co':
        return None, None
    
    path_parts = parsed_url.path.strip('/').split('/')
    if len(path_parts) < 2:
        return None, None
    
    repo_id = f"{path_parts[0]}/{path_parts[1]}"
    
    filename = None
    if '/resolve/' in url and len(path_parts) > 3:
        filename = '/'.join(path_parts[4:])
    elif '/blob/' in url and len(path_parts) > 3:
        filename = '/'.join(path_parts[4:])

    return repo_id, filename

@handle_errors_manager
def m_download(line, log=False, unzip=False):
    parts = shlex.split(line)
    if not parts: return False

    url_original = parts[0]

    current_home_path = Path(js.read(SETTINGS_PATH_IN_MANAGER, 'ENVIRONMENT.home_path', str(Path.home())))
    dst_dir = Path(parts[1] if len(parts) > 1 else str(current_home_path))
    filename_original = parts[2] if len(parts) > 2 else None

    filename_to_use = filename_original or unquote(Path(urlparse(url_original).path).name)

    is_hf_url = 'huggingface.co' in url_original
    
    original_cwd = Path.cwd()
    download_successful = False
    try:
        dst_dir.mkdir(parents=True, exist_ok=True)

        if is_hf_url:
            log_manager('info', f"Using Hugging Face Hub downloader for: {filename_to_use}")
            repo_id, hf_filename = parse_hf_url(url_original)
            if not repo_id or not hf_filename:
                log_manager('error', f"Could not parse Hugging Face URL: {url_original}")
                return False
            
            _, hf_token = get_tokens_manager()
            try:
                log_manager('progress', f"Downloading {filename_to_use} via HF Hub...", data={'percentage': 0})
                downloaded_cache_path = hf_hub_download(
                    repo_id=repo_id,
                    filename=hf_filename,
                    token=hf_token or None,
                    cache_dir=ANXETY_ROOT_MANAGER / '.hf_cache'
                )
                log_manager('progress', f"Downloading {filename_to_use} via HF Hub...", data={'percentage': 50})
                
                final_destination = dst_dir / filename_to_use
                shutil.copy(downloaded_cache_path, final_destination)
                log_manager('progress', f"Downloading {filename_to_use} via HF Hub...", data={'percentage': 100})
                download_successful = True

            except (GatedRepoError, HfHubHTTPError) as e:
                log_manager('error', f"Hugging Face Hub download failed: {e}")
            except Exception as e:
                log_manager('error', f"An unexpected error occurred with HF Hub download: {e}")

        elif filename_to_use.lower().endswith(('.zip', '.tar', '.gz', '.rar')):
            log_manager('info', f"Using reliable download (curl) for generic archive: {filename_to_use}")
            target_file_path = dst_dir / filename_to_use
            curl_command = ["curl", "--location", "--progress-bar", "-o", str(target_file_path), url_original]
            process = subprocess.run(curl_command, capture_output=True, text=True, encoding='utf-8', errors='replace')
            if process.returncode == 0 and target_file_path.exists() and target_file_path.stat().st_size > 0:
                download_successful = True
            else:
                log_manager('error', f"curl download failed. Exit code: {process.returncode}. Stderr: {process.stderr}")
        
        else:
            log_manager('info', f"Using aria2c for download: {filename_to_use}")
            url_for_aria = clean_url_manager(url_original)
            if not url_for_aria:
                log_manager('error', f"URL cleaning failed for aria2c path: {url_original}"); return False

            os.chdir(dst_dir)
            aria2_command = f"aria2c --console-log-level=warn -c -x 16 -s 16 -k 1M -j 5 --summary-interval=1 -o '{filename_to_use}' '{url_for_aria}'"
            process = subprocess.run(shlex.split(aria2_command), capture_output=True, text=True)
            if process.returncode == 0:
                download_successful = True
            else:
                log_manager('error', f"aria2c download failed. Exit: {process.returncode}. Stderr: {process.stderr}")
            os.chdir(original_cwd)

        if download_successful:
            log_manager('success', f"✅ Download complete: {dst_dir / filename_to_use}")
            if unzip and filename_to_use.endswith('.zip'):
                log_manager('info', f"Unzipping {filename_to_use}...")
                with zipfile.ZipFile(dst_dir / filename_to_use, 'r') as zip_ref:
                    zip_ref.extractall(dst_dir)
                os.remove(dst_dir / filename_to_use)
                log_manager('success', f"✅ Unzipped and removed {filename_to_use}.")
            return True
        else:
            log_manager('error', f"❌ Download ultimately failed for {filename_to_use}")
            return False
            
    finally:
        if Path.cwd() != original_cwd: os.chdir(original_cwd)
    return download_successful