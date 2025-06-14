# /content/ANXETY/modules/Manager.py (Explicit Filename Check for Curl)

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

@handle_errors_manager
def clean_url_manager(url_input: str) -> str:
    if 'civitai.com/api/download/models' in url_input: return url_input
    if 'civitai.com/models/' in url_input:
        cai_token, _ = get_tokens_manager()
        api = CivitAiAPI(cai_token)
        try:
            version_data = api.get_data(url_input) 
            if version_data and version_data.get('files'):
                primary_file = next((f for f in version_data['files'] if f.get('primary')), None)
                file_to_download = primary_file or version_data['files'][0]
                return file_to_download.get('downloadUrl')
        except Exception: pass
        return url_input 
    elif 'huggingface.co' in url_input:
        if '/blob/' in url_input: return url_input.replace('/blob/', '/resolve/').split('?')[0]
        return url_input 
    elif 'github.com' in url_input and '/blob/' in url_input:
        return url_input.replace('/blob/', '/raw/')
    return url_input

@handle_errors_manager
def m_download(line, log=False, unzip=False):
    parts = shlex.split(line)
    if not parts: return False
    
    url_original = parts[0]
    
    current_home_path = Path(js.read(SETTINGS_PATH_IN_MANAGER, 'ENVIRONMENT.home_path', str(Path.home())))
    dst_dir = Path(parts[1] if len(parts) > 1 else str(current_home_path))
    filename_original = parts[2] if len(parts) > 2 else None
    
    url_for_processing = url_original
    filename_to_use = filename_original or unquote(Path(urlparse(url_for_processing).path).name)

    # --- FINAL STRATEGY: Check filename for known VENV or WebUI zip patterns ---
    is_critical_hf_download = (
        "python31017-venv" in filename_to_use or
        "python31112-venv" in filename_to_use or
        any(ui_zip in filename_to_use for ui_zip in ["A1111.zip", "Forge.zip", "ReForge.zip", "Classic.zip", "ComfyUI.zip", "SD-UX.zip"])
    )

    original_cwd = Path.cwd()
    download_successful = False
    try:
        dst_dir.mkdir(parents=True, exist_ok=True)
        
        if is_critical_hf_download:
            log_manager('info', f"Using reliable download (curl) for critical file: {filename_to_use}")
            target_file_path = dst_dir / filename_to_use
            curl_command = ["curl", "--location", "--progress-bar", "-o", str(target_file_path), url_original]
            log_manager('progress', f"Downloading {filename_to_use} with curl...", data={'percentage': 0, 'raw_line': 'curl started'})
            
            process = subprocess.run(curl_command, capture_output=True, text=True, encoding='utf-8', errors='replace')
            
            if process.returncode == 0 and target_file_path.exists() and target_file_path.stat().st_size > 0:
                log_manager('progress', f"Downloading {filename_to_use} with curl...", data={'percentage': 100, 'raw_line': 'curl finished'})
                download_successful = True
            else:
                log_manager('error', f"curl download failed for {filename_to_use}. Exit code: {process.returncode}. Stderr: {process.stderr}")
        else:
            # Use aria2c for other downloads (e.g., Civitai models)
            url_for_aria = clean_url_manager(url_original)
            if not url_for_aria:
                log_manager('error', f"URL cleaning failed for aria2c path: {url_original}"); return False

            os.chdir(dst_dir)
            _, hf_token = get_tokens_manager()
            aria2_command_list = ['aria2c','--header="User-Agent: Mozilla/5.0"','--allow-overwrite=true','--stderr=true','-c','-x16','-s16','-k1M','-j5','--summary-interval=1','--console-log-level=warn','-o',filename_to_use,url_for_aria]
            if hf_token and 'huggingface.co' in url_for_aria:
                aria2_command_list.insert(1, f'--header=Authorization: Bearer {hf_token}')
            
            progress_pattern = re.compile(r"\[#[a-f0-9]+\s+.*\s*\((\d+)%\)[^\]]*\]")
            process = subprocess.Popen(aria2_command_list, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace')
            for Rline in iter(process.stdout.readline, ''):
                Rline = Rline.strip();
                if not Rline: continue
                if match := progress_pattern.search(Rline):
                    log_manager('progress', f"Downloading {filename_to_use}", data={'percentage': int(match.group(1)), 'raw_line': Rline})
                elif log: log_manager('debug', Rline)
            process.wait()
            if process.returncode == 0: download_successful = True
            else: log_manager('error', f"aria2c download failed for {filename_to_use}. Exit code: {process.returncode}.")
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

def m_clone(command, log_param=False):
    try:
        subprocess.run(shlex.split(command), check=True, capture_output=not log_param)
        log_manager('success', f"Clone successful: {command.split()[-1]}")
    except Exception as e:
        log_manager('error', f"Clone failed for {command.split()[-1]}: {e}")
