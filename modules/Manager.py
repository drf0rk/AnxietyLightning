# /content/ANXETY/modules/Manager.py (Single Line Progress Edition)

import os
import sys
from pathlib import Path
from urllib.parse import urlparse, unquote
import subprocess
import requests # Ensure requests is imported if clean_url uses it
import zipfile
import shlex
import re # For parsing aria2c output
import json # For structured logging

# --- Self-aware pathing ---
# This ensures the script can find other modules if this Manager.py
# is ever called in a context where ANXETY_ROOT isn't already in sys.path
try:
    ANXETY_ROOT_MANAGER = Path(__file__).resolve().parents[1]
except NameError:
    ANXETY_ROOT_MANAGER = Path('/content/ANXETY')

if str(ANXETY_ROOT_MANAGER) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT_MANAGER))
# ---

from modules.CivitaiAPI import CivitAiAPI # Assuming CivitaiAPI is in modules
import modules.json_utils as js

# --- Constants ---
CD = os.chdir
HOME = Path.home() # This might be overridden by settings in the calling script
SETTINGS_PATH_IN_MANAGER = ANXETY_ROOT_MANAGER / 'settings.json' # Manager's own ref

# --- Structured Logger for Manager.py ---
def log_manager(level, message, data=None):
    """Prints a structured JSON log entry from Manager.py."""
    log_entry = {"type": "log", "level": level, "message": message, "data": data or {}}
    # This print will be captured by the calling script's (e.g., downloading-en.py) Popen stdout
    print(json.dumps(log_entry), flush=True)

def get_tokens_manager():
    # Read from its own reference to settings, or fall back if called very early
    cai_token = js.read(SETTINGS_PATH_IN_MANAGER, 'WIDGETS.civitai_token', '65b66176dcf284b266579de57fbdc024')
    hf_token = js.read(SETTINGS_PATH_IN_MANAGER, 'WIDGETS.huggingface_token', '')
    return cai_token, hf_token

def handle_errors_manager(func):
    def wrapper(*args, **kwargs):
        try: return func(*args, **kwargs)
        except Exception as e:
            log_manager('error', f"Manager Error in {func.__name__}: {e}", data={'args': args, 'kwargs': kwargs})
            return None
    return wrapper

@handle_errors_manager
def clean_url_manager(url):
    cai_token, _ = get_tokens_manager()
    if 'civitai.com/models/' in url:
        # Ensure CivitAiAPI is initialized correctly here if needed
        # This might need adjustment if CivitAiAPI relies on a global instance
        api = CivitAiAPI(cai_token) 
        version_id = api.get_version_id_from_url(url)
        if not version_id: return url # Fallback if ID not found
        version_data = api.get_data(url) # get_data expects version URL or ID
        if version_data and version_data.get('files'):
            # Prioritize primary file, then first file
            primary_file = next((f for f in version_data['files'] if f.get('primary')), None)
            file_to_download = primary_file or version_data['files'][0]
            return file_to_download.get('downloadUrl')
        return url # Fallback
    elif 'huggingface.co' in url:
        return url.replace('/blob/', '/resolve/').split('?')[0]
    elif 'github.com' in url:
        return url.replace('/blob/', '/raw/')
    return url

@handle_errors_manager
def m_download(line, log=False, unzip=False): # log parameter from calling script determines if m_download itself logs verbosely
    parts = shlex.split(line)
    if not parts: return
    
    url_original = parts[0]
    # Resolve HOME based on settings if available, otherwise use Manager's default
    # This requires downloading-en.py to have saved 'home_path'
    current_home_path = Path(js.read(SETTINGS_PATH_IN_MANAGER, 'ENVIRONMENT.home_path', str(Path.home())))
    
    dst_dir_str = parts[1] if len(parts) > 1 else str(current_home_path)
    dst_dir = Path(dst_dir_str)
    
    filename_original = parts[2] if len(parts) > 2 else None # Keep original filename if specified
    
    clean_url_val = clean_url_manager(url_original)
    if not clean_url_val: 
        log_manager('error', f"Could not clean URL: {url_original}")
        return

    # Determine filename: use specified, else from cleaned URL, else from original URL
    filename_to_use = filename_original or unquote(Path(urlparse(clean_url_val).path).name)
    if not Path(filename_to_use).suffix: # If no extension, try to get from original URL
        original_suffix_name = unquote(Path(urlparse(url_original).path).name)
        if Path(original_suffix_name).suffix:
            filename_to_use = original_suffix_name


    original_cwd = Path.cwd()
    try:
        dst_dir.mkdir(parents=True, exist_ok=True)
        os.chdir(dst_dir)
        
        _, hf_token = get_tokens_manager()
        # Aria2c arguments - ensure we don't use --console-log-level=error if we want to parse progress
        aria2_args = [
            'aria2c',
            '--header="User-Agent: Mozilla/5.0"',
            '--allow-overwrite=true',
            '--stderr=true', # Important for capturing all output
            '-c', '-x16', '-s16', '-k1M', '-j5',
            '--summary-interval=1', # Get updates every 1 second
            '--console-log-level=warn', # Changed from error to get progress
            f'-d', str(dst_dir), # Use absolute path for aria2c
            f'-o', filename_to_use,
            clean_url_val
        ]
        if hf_token and 'huggingface.co' in clean_url_val:
            aria2_args.insert(1, f'--header="Authorization: Bearer {hf_token}"')

        # Regex to capture standard aria2c progress line
        # Example: "[#7f8e35 1.8GiB/1.9GiB(90%) CN:16 DL:220MiB ETA:1s]"
        progress_pattern = re.compile(r"\[#[a-f0-9]+\s+([0-9.]+)([GMKiB]+)/([0-9.]+)([GMKiB]+)\s*\((\d+)%\)[^\]]*DL:([0-9.]+)([GMKiB]+)[^\]]*\]")

        process = subprocess.Popen(aria2_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace')
        
        log_manager('info', f"Starting download: {filename_to_use}") # Initial message

        for Rline in iter(process.stdout.readline, ''):
            Rline = Rline.strip()
            if not Rline: continue

            match = progress_pattern.search(Rline)
            if match:
                # Parsed values: current_size_val, current_size_unit, total_size_val, total_size_unit, percentage, speed_val, speed_unit
                percentage = match.group(5)
                # Use the 'progress' level for these structured updates
                log_manager('progress', f"Downloading {filename_to_use}", data={'percentage': int(percentage), 'raw_line': Rline})
            elif log: # Only print non-progress lines if verbose logging is on for m_download
                log_manager('debug', Rline) # Log other aria2c output as debug

        process.wait()
        if process.returncode != 0:
            log_manager('error', f"Download failed for {filename_to_use}. aria2c exited with {process.returncode}.")
        else:
            log_manager('success', f"✅ Download complete: {filename_to_use}")
            if unzip and filename_to_use.endswith('.zip'):
                log_manager('info', f"Unzipping {filename_to_use}...")
                with zipfile.ZipFile(filename_to_use, 'r') as zip_ref:
                    zip_ref.extractall()
                os.remove(filename_to_use)
                log_manager('success', f"✅ Unzipped and removed {filename_to_use}.")

    finally:
        os.chdir(original_cwd)

def m_clone(command, log_param=False): # 'log' parameter renamed to 'log_param' to avoid conflict
    try:
        subprocess.run(shlex.split(command), check=True, capture_output=not log_param)
        log_manager('success', f"Clone successful: {command.split()[-1]}")
    except Exception as e:
        log_manager('error', f"Clone failed for {command.split()[-1]}: {e}")
