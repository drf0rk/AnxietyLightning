# /content/ANXETY/modules/Manager.py (VENV Download Robustness)

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
import time # For retries

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

# --- Constants ---
SETTINGS_PATH_IN_MANAGER = ANXETY_ROOT_MANAGER / 'settings.json'

# --- Structured Logger for Manager.py ---
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
            return None # Or False for functions expecting a boolean success
    return wrapper

@handle_errors_manager
def clean_url_manager(url):
    cai_token, _ = get_tokens_manager()
    if 'civitai.com/models/' in url:
        api = CivitAiAPI(cai_token)
        version_id = api.get_version_id_from_url(url)
        if not version_id: return url
        version_data = api.get_data(url)
        if version_data and version_data.get('files'):
            primary_file = next((f for f in version_data['files'] if f.get('primary')), None)
            file_to_download = primary_file or version_data['files'][0]
            return file_to_download.get('downloadUrl')
        return url
    elif 'huggingface.co' in url:
        return url.replace('/blob/', '/resolve/').split('?')[0]
    elif 'github.com' in url:
        return url.replace('/blob/', '/raw/')
    return url

@handle_errors_manager
def m_download(line, log=False, unzip=False):
    parts = shlex.split(line)
    if not parts: return False # Indicate failure
    
    url_original = parts[0]
    current_home_path = Path(js.read(SETTINGS_PATH_IN_MANAGER, 'ENVIRONMENT.home_path', str(Path.home())))
    dst_dir = Path(parts[1] if len(parts) > 1 else str(current_home_path))
    filename_original = parts[2] if len(parts) > 2 else None
    
    clean_url_val = clean_url_manager(url_original)
    if not clean_url_val: 
        log_manager('error', f"Could not clean URL: {url_original}")
        return False

    filename_to_use = filename_original or unquote(Path(urlparse(clean_url_val).path).name)
    if not Path(filename_to_use).suffix:
        original_suffix_name = unquote(Path(urlparse(url_original).path).name)
        if Path(original_suffix_name).suffix:
            filename_to_use = original_suffix_name

    original_cwd = Path.cwd()
    try:
        dst_dir.mkdir(parents=True, exist_ok=True)
        os.chdir(dst_dir) # Change to target directory for aria2c
        
        _, hf_token = get_tokens_manager()
        
        # Base aria2c command arguments
        aria2_base_args = [
            'aria2c',
            '--allow-overwrite=true',
            '--stderr=true',
            '-c', '-x16', '-s16', '-k1M', '-j5',
            '--summary-interval=1',
            '--console-log-level=warn',
            # Removed -d and -o, as we chdir to dst_dir and aria2c will use filename from URL
        ]

        # Add headers - crucial for Hugging Face
        headers = [
            '--header="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"',
            '--header="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"',
            '--header="Accept-Language: en-US,en;q=0.9"',
            '--header="Connection: keep-alive"',
        ]
        aria2_command_with_headers = aria2_base_args + headers

        if hf_token and 'huggingface.co' in clean_url_val:
            aria2_command_with_headers.append(f'--header="Authorization: Bearer {hf_token}"')
        
        # Add output filename and URL at the end
        aria2_command_full = aria2_command_with_headers + [f'-o', filename_to_use, clean_url_val]

        progress_pattern = re.compile(r"\[#[a-f0-9]+\s+([0-9.]+)([GMKiB]+)/([0-9.]+)([GMKiB]+)\s*\((\d+)%\)[^\]]*DL:([0-9.]+)([GMKiB]+)[^\]]*\]")
        
        max_retries = 2 # Try original + 2 retries
        for attempt in range(max_retries + 1):
            log_manager('info', f"Starting download (Attempt {attempt + 1}/{max_retries + 1}): {filename_to_use}")
            
            # Use shlex.join for safety if constructing command string, or pass list directly
            process = subprocess.Popen(aria2_command_full, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace')
            
            last_progress_line = ""
            for Rline in iter(process.stdout.readline, ''):
                Rline = Rline.strip()
                if not Rline: continue

                match = progress_pattern.search(Rline)
                if match:
                    percentage = match.group(5)
                    # Update last_progress_line to simulate overwriting for the log
                    last_progress_line = f"Downloading {filename_to_use} ({percentage}%) - {Rline}"
                    log_manager('progress', last_progress_line, data={'percentage': int(percentage), 'raw_line': Rline})
                elif log: # Only print non-progress lines if verbose logging is on
                    log_manager('debug', Rline)
            
            process.wait()
            if process.returncode == 0:
                log_manager('success', f"✅ Download complete: {filename_to_use}")
                if unzip and filename_to_use.endswith('.zip'):
                    log_manager('info', f"Unzipping {filename_to_use}...")
                    with zipfile.ZipFile(filename_to_use, 'r') as zip_ref:
                        zip_ref.extractall() # Extracts to current dir (dst_dir)
                    os.remove(filename_to_use)
                    log_manager('success', f"✅ Unzipped and removed {filename_to_use}.")
                return True # Success
            else:
                log_manager('error', f"Download attempt {attempt + 1} failed for {filename_to_use}. aria2c exited with {process.returncode}.")
                if attempt < max_retries:
                    log_manager('info', "Retrying in 5 seconds...")
                    time.sleep(5)
                else:
                    log_manager('error', f"All download attempts failed for {filename_to_use}.")
                    return False # All retries failed

    finally:
        os.chdir(original_cwd)
    return False # Should not be reached if logic is correct

def m_clone(command, log_param=False):
    try:
        subprocess.run(shlex.split(command), check=True, capture_output=not log_param)
        log_manager('success', f"Clone successful: {command.split()[-1]}")
    except Exception as e:
        log_manager('error', f"Clone failed for {command.split()[-1]}: {e}")
