# /content/ANXETY/modules/Manager.py (Definitive Version)

import os
import sys
from pathlib import Path
from urllib.parse import urlparse
import subprocess
import requests
import zipfile
import shlex

# --- Self-aware pathing to allow sibling imports ---
try:
    # When this module is imported, its own location can be used to find the modules folder
    MODULES_DIR = Path(__file__).resolve().parent
    if str(MODULES_DIR) not in sys.path:
        sys.path.insert(0, str(MODULES_DIR))
except NameError:
    # Fallback for some execution environments
    if 'modules' not in sys.path[0]:
        sys.path.insert(0, 'modules')
# ---

from CivitaiAPI import CivitAiAPI
import json_utils as js

# --- The rest of the file remains the same ---
CD = os.chdir
HOME = Path.home()
ANXETY_ROOT = HOME / 'ANXETY'
SETTINGS_PATH = ANXETY_ROOT / 'settings.json'

def get_tokens():
    cai_token = js.read(SETTINGS_PATH, 'WIDGETS.civitai_token') or '65b66176dcf284b266579de57fbdc024'
    hf_token = js.read(SETTINGS_PATH, 'WIDGETS.huggingface_token') or ''
    return cai_token, hf_token

def log_message(message, log=False):
    if log: print(f"{message}")

def handle_errors(func):
    def wrapper(*args, **kwargs):
        try: return func(*args, **kwargs)
        except Exception as e:
            log_message(f"> \033[31m[Error]:\033[0m {e}", kwargs.get('log', False))
            return None
    return wrapper

def execute_shell_command(command, log):
    if log:
        subprocess.run(shlex.split(command), check=True)
    else:
        subprocess.run(shlex.split(command), check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

@handle_errors
def clean_url(url):
    cai_token, _ = get_tokens()
    if 'civitai.com/models/' in url:
        api = CivitAiAPI(cai_token)
        data = api.validate_download(url)
        return data.download_url if data else None
    elif 'huggingface.co' in url:
        return url.replace('/blob/', '/resolve/').split('?')[0]
    elif 'github.com' in url:
        return url.replace('/blob/', '/raw/')
    return url

def download_with_aria2(url, filename, log):
    _, hf_token = get_tokens()
    aria2_args = '--header="User-Agent: Mozilla/5.0" --allow-overwrite=true --console-log-level=error --stderr=true -c -x16 -s16 -k1M -j5'
    if hf_token and 'huggingface.co' in url:
        aria2_args += f' --header="Authorization: Bearer {hf_token}"'
    command = f"aria2c {aria2_args} -d \"{Path.cwd()}\" -o \"{filename}\" \"{url}\""
    execute_shell_command(command, log)

@handle_errors
def m_download(line, log=False, unzip=False):
    parts = shlex.split(line)
    if not parts: return
    
    url = parts[0]
    dst_dir = Path(parts[1]) if len(parts) > 1 else Path.cwd()
    filename = parts[2] if len(parts) > 2 else Path(urlparse(url).path).name
    
    clean_url_val = clean_url(url)
    if not clean_url_val: return

    original_cwd = Path.cwd()
    try:
        dst_dir.mkdir(parents=True, exist_ok=True)
        os.chdir(dst_dir)
        download_with_aria2(clean_url_val, filename, log)
        if unzip and filename.endswith('.zip'):
            with zipfile.ZipFile(filename, 'r') as zip_ref:
                zip_ref.extractall()
            os.remove(filename)
    finally:
        os.chdir(original_cwd)

def m_clone(command, log=False):
    execute_shell_command(command, log)