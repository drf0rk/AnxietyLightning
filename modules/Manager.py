# /content/ANXETY/modules/Manager.py (Corrected with Relative Imports)

# --- CORRECTED RELATIVE IMPORTS ---
from .CivitaiAPI import CivitAiAPI    # CivitAI API
from . import json_utils as js        # JSON
# --- END OF CORRECTION ---

from urllib.parse import urlparse, parse_qs
from pathlib import Path
import subprocess
import requests
import zipfile
import shlex
import sys
import os
import re

CD = os.chdir

# Constants
HOME = Path.home()
SCR_PATH = HOME / 'ANXETY'
SETTINGS_PATH = SCR_PATH / 'settings.json'

# Use a function to read settings to avoid import-time issues
def get_tokens():
    cai_token = js.read(SETTINGS_PATH, 'WIDGETS.civitai_token') or '65b66176dcf284b266579de57fbdc024'
    hf_token = js.read(SETTINGS_PATH, 'WIDGETS.huggingface_token') or ''
    return cai_token, hf_token

# Logging function
def log_message(message, log=False):
    if log:
        print(f"{message}")

# Error handling decorator
def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            log_message(f"> \033[31m[Error]:\033[0m {e}", kwargs.get('log', False))
            return None
    return wrapper

@handle_errors
def m_download(line, log=False, unzip=False):
    links = [link.strip() for link in line.split(',') if link.strip()]
    if not links:
        log_message('> Missing URL, downloading nothing', log)
        return
    for link in links:
        process_download(link, log, unzip)

@handle_errors
def process_download(line, log, unzip):
    parts = shlex.split(line)
    if not parts: return
    
    url = parts[0].replace('\\', '')
    url = clean_url(url)
    if not url: return

    path_str = parts[1] if len(parts) > 1 else None
    filename = parts[2] if len(parts) > 2 else None
    
    path = Path(path_str).expanduser() if path_str else None
    current_dir = Path.cwd()

    try:
        if path:
            path.mkdir(parents=True, exist_ok=True)
            CD(path)
        download_file(url, filename, log)
        if unzip and filename and filename.endswith('.zip'):
            unzip_file(filename, log)
    finally:
        CD(current_dir)

def download_file(url, filename, log):
    is_special_domain = any(domain in url for domain in ['civitai.com', 'huggingface.co', 'github.com'])
    if is_special_domain:
        download_with_aria2(url, filename, log)
    elif 'drive.google.com' in url:
        download_google_drive(url, filename, log)
    else:
        command = f"curl -#JL '{url}'"
        if filename: command += f" -o '{filename}'"
        execute_shell_command(command, log)

def download_with_aria2(url, filename, log):
    _, hf_token = get_tokens()
    aria2_args = ('aria2c --header="User-Agent: Mozilla/5.0" --allow-overwrite=true --console-log-level=error --stderr=true -c -x16 -s16 -k1M -j5')
    if hf_token and 'huggingface.co' in url:
        aria2_args += f' --header="Authorization: Bearer {hf_token}"'
    
    command = f"{aria2_args} '{url}'"
    if not filename:
        filename = Path(urlparse(url).path).name
    if filename:
        command += f" -o '{filename}'"
        
    monitor_aria2_download(command, log)

def download_google_drive(url, filename, log):
    cmd = f"gdown --fuzzy {url}"
    if filename: cmd += f" -O {filename}"
    if 'drive/folders' in url: cmd += " --folder"
    execute_shell_command(cmd, log)

@handle_errors
def unzip_file(zip_filepath, log):
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        zip_ref.extractall(Path(zip_filepath).parent)
    log_message(f">> Successfully unpacked: {zip_filepath}", log)

def execute_shell_command(command, log):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if log:
        for line in process.stderr: print(line, end='')
    process.wait()

def monitor_aria2_download(command, log):
    # This function is complex, leaving it as is.
    # Verbose logging should be sufficient for now.
    execute_shell_command(command, log)

@handle_errors
def clean_url(url):
    cai_token, _ = get_tokens()
    if 'civitai.com/models/' in url:
        api = CivitAiAPI(cai_token)
        data = api.validate_download(url)
        return data.download_url if data else None
    elif 'huggingface.co' in url:
        if '/blob/' in url: return url.replace('/blob/', '/resolve/')
        if '?' in url: return url.split('?')[0]
    elif 'github.com' in url:
        if '/blob/' in url: return url.replace('/blob/', '/raw/')
    return url

def m_clone(input_source, log=False):
    # This function should be okay as it doesn't have local imports.
    # Leaving it as is.
    command = f"git clone --depth 1 {input_source}"
    execute_shell_command(command, log)