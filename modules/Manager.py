# /content/ANXETY/modules/Manager.py (Targeted curl for HF, Aria2c for others)

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
def clean_url_manager(url):
    cai_token, _ = get_tokens_manager()
    if 'civitai.com/models/' in url and 'api/download/models' not in url: # Process only model page URLs
        api = CivitAiAPI(cai_token)
        version_id = api.get_version_id_from_url(url)
        if not version_id: return url
        version_data = api.get_data(url) # get_data expects version URL or ID
        if version_data and version_data.get('files'):
            primary_file = next((f for f in version_data['files'] if f.get('primary')), None)
            file_to_download = primary_file or version_data['files'][0]
            return file_to_download.get('downloadUrl')
        return url
    elif 'huggingface.co' in url and '/blob/' in url: # Only transform blob URLs
        return url.replace('/blob/', '/resolve/').split('?')[0]
    elif 'github.com' in url and '/blob/' in url: # Only transform blob URLs
        return url.replace('/blob/', '/raw/')
    return url # Return Civitai API URLs or other direct links as is

@handle_errors_manager
def m_download(line, log=False, unzip=False): # log param controls Manager's own verbose logging
    parts = shlex.split(line)
    if not parts: return False
    
    url_original = parts[0]
    current_home_path = Path(js.read(SETTINGS_PATH_IN_MANAGER, 'ENVIRONMENT.home_path', str(Path.home())))
    dst_dir = Path(parts[1] if len(parts) > 1 else str(current_home_path))
    filename_original = parts[2] if len(parts) > 2 else None
    
    clean_url_val = clean_url_manager(url_original)
    if not clean_url_val: 
        log_manager('error', f"Could not clean URL: {url_original}")
        return False

    filename_to_use = filename_original or unquote(Path(urlparse(clean_url_val).path).name)
    if not Path(filename_to_use).suffix and clean_url_val == url_original: # If cleaning didn't change URL and no ext
        original_suffix_name = unquote(Path(urlparse(url_original).path).name)
        if Path(original_suffix_name).suffix:
            filename_to_use = original_suffix_name
    
    # Ensure filename has an extension if it's a common model/archive type, otherwise aria2c might misbehave
    common_extensions = ['.safetensors', '.ckpt', '.pt', '.bin', '.zip', '.tar', '.gz', '.lz4', '.yaml', '.json']
    if not any(filename_to_use.endswith(ext) for ext in common_extensions) and any(url_original.endswith(ext) for ext in common_extensions):
        # Attempt to derive extension from original URL if filename_to_use lacks it
        derived_filename_from_original_url = unquote(Path(urlparse(url_original).path).name)
        if Path(derived_filename_from_original_url).suffix:
             filename_to_use = derived_filename_from_original_url


    original_cwd = Path.cwd()
    download_successful = False
    try:
        dst_dir.mkdir(parents=True, exist_ok=True)
        
        # --- STRATEGY CHANGE: Use curl for specific Hugging Face /resolve/main/ URLs ---
        # This targets VENVs and WebUI zips primarily.
        is_hf_resolve_download = "huggingface.co" in clean_url_val and "/resolve/main/" in clean_url_val
        
        if is_hf_resolve_download:
            log_manager('info', f"Using curl for Hugging Face direct download: {filename_to_use}")
            target_file_path = dst_dir / filename_to_use
            curl_command = ["curl", "--location", "--progress-bar", "-o", str(target_file_path), clean_url_val]
            # curl progress is shown directly in notebook, less structured for Gradio log
            log_manager('progress', f"Downloading {filename_to_use} with curl...", data={'percentage': 0, 'raw_line': 'curl started'})
            
            # Run curl and stream its output for basic progress indication if possible
            process = subprocess.Popen(curl_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace')
            for Rline in iter(process.stdout.readline, ''): # Show curl's own output
                Rline = Rline.strip()
                if Rline: log_manager('debug', f"curl: {Rline}") # Log curl output

            process.wait()
            if process.returncode == 0 and target_file_path.exists() and target_file_path.stat().st_size > 0:
                log_manager('progress', f"Downloading {filename_to_use} with curl...", data={'percentage': 100, 'raw_line': 'curl finished'})
                download_successful = True
            else:
                log_manager('error', f"curl download failed for {filename_to_use}. Exit code: {process.returncode}")
                download_successful = False
        else:
            # Use aria2c for other downloads (Civitai, general models)
            os.chdir(dst_dir)
            _, hf_token = get_tokens_manager() # hf_token might still be useful for non-resolve HF URLs
            aria2_base_args = ['aria2c','--allow-overwrite=true','--stderr=true','-c','-x16','-s16','-k1M','-j5','--summary-interval=1','--console-log-level=warn']
            headers = ['--header="User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"'] # Simplified headers for general case
            aria2_command_with_headers = aria2_base_args + headers
            if hf_token and 'huggingface.co' in clean_url_val: # For any other HF links not covered by curl
                aria2_command_with_headers.append(f'--header="Authorization: Bearer {hf_token}"')
            aria2_command_full = aria2_command_with_headers + [f'-o', filename_to_use, clean_url_val]
            
            progress_pattern = re.compile(r"\[#[a-f0-9]+\s+([0-9.]+)([GMKiB]+)/([0-9.]+)([GMKiB]+)\s*\((\d+)%\)[^\]]*DL:([0-9.]+)([GMKiB]+)[^\]]*\]")
            max_retries = 2
            for attempt in range(max_retries + 1):
                log_manager('info', f"Starting aria2c download (Attempt {attempt + 1}/{max_retries + 1}): {filename_to_use}")
                process = subprocess.Popen(aria2_command_full, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace')
                for Rline in iter(process.stdout.readline, ''):
                    Rline = Rline.strip();
                    if not Rline: continue
                    if match := progress_pattern.search(Rline):
                        log_manager('progress', f"Downloading {filename_to_use}", data={'percentage': int(match.group(5)), 'raw_line': Rline})
                    elif log: log_manager('debug', Rline)
                process.wait()
                if process.returncode == 0: download_successful = True; break
                else:
                    log_manager('error', f"aria2c attempt {attempt + 1} failed for {filename_to_use}. Exit code: {process.returncode}.")
                    if attempt < max_retries: time.sleep(5)
                    else: log_manager('error', f"All aria2c attempts failed for {filename_to_use}.")
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
        if Path.cwd() != original_cwd:
            os.chdir(original_cwd)
    return download_successful

def m_clone(command, log_param=False):
    try:
        subprocess.run(shlex.split(command), check=True, capture_output=not log_param)
        log_manager('success', f"Clone successful: {command.split()[-1]}")
    except Exception as e:
        log_manager('error', f"Clone failed for {command.split()[-1]}: {e}")
