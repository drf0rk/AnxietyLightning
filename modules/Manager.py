# /content/ANXETY/modules/Manager.py (vRobust - System Unzip)

import os
import sys
from pathlib import Path
from urllib.parse import urlparse, unquote
import subprocess
import shlex
import json
import time
import shutil
from huggingface_hub import hf_hub_download
from huggingface_hub.utils import GatedRepoError, HfHubHTTPError

# ... (rest of the file is the same until the m_download function) ...

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

        # Download logic remains the same...
        # ... (HF Hub, curl, aria2c logic) ...

        if download_successful:
            log_manager('success', f"✅ Download complete: {dst_dir / filename_to_use}")
            if unzip and filename_to_use.endswith('.zip'):
                log_manager('info', f"Unzipping {filename_to_use}...")
                
                zip_path = dst_dir / filename_to_use
                # The destination for the unzipped content is a directory named after the zip file (without the .zip)
                unzip_destination = dst_dir / zip_path.stem
                unzip_destination.mkdir(parents=True, exist_ok=True)

                # Use system unzip for robustness
                unzip_command = ["unzip", "-o", str(zip_path), "-d", str(unzip_destination)]
                unzip_process = subprocess.run(unzip_command, check=True, capture_output=True, text=True)
                
                os.remove(zip_path)
                log_manager('success', f"✅ Unzipped and removed {filename_to_use}.")

            return True
        else:
            log_manager('error', f"❌ Download ultimately failed for {filename_to_use}")
            return False
            
    finally:
        if Path.cwd() != original_cwd: os.chdir(original_cwd)
    return download_successful