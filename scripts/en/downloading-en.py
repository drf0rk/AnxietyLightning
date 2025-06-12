# /content/ANXETY/scripts/en/downloading-en.py (Refactored for Backend-Only Operations)

import os
import sys
from pathlib import Path
import subprocess
import re
from urllib.parse import urlparse, unquote
import shlex
import shutil

# --- Pathing & Imports ---
# Ensure ANXETY_ROOT is correctly set for relative imports
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[2] # Adjust parent level if this file is now in /scripts/en/
except NameError:
    ANXETY_ROOT = Path('/content/ANXETY') # Fallback for direct execution testing

if str(ANXETY_ROOT) not in sys.path: sys.path.insert(0, str(ANXETY_ROOT))
if str(ANXETY_ROOT / 'modules') not in sys.path: sys.path.insert(0, str(ANXETY_ROOT / 'modules'))

import modules.json_utils as js
from modules.Manager import m_download

# Constants (loaded from settings.json or derived defaults)
SETTINGS_PATH = ANXETY_ROOT / 'settings.json'

# --- Load settings needed by this script ---
# We load the entire settings structure here to ensure all necessary paths and flags are available.
def load_all_settings(path):
    try:
        env_settings = js.read(path, 'ENVIRONMENT', {})
        widget_settings = js.read(path, 'WIDGETS', {})
        webui_settings = js.read(path, 'WEBUI', {})
        return {
            **env_settings,
            **widget_settings,
            **webui_settings
        }
    except Exception as e:
        print(f"❌ Error loading settings in downloading-en.py: {e}")
        return {}

settings = load_all_settings(SETTINGS_PATH)
# Make settings available as local variables for convenience
locals().update(settings)

# Ensure HOME is correctly defined from settings, or fallback
HOME = Path(settings.get('home_path', '/content'))
VENV_PATH = HOME / 'venv'

# This should be dynamically read from settings if possible, or defined
# based on the selected UI in settings.json to ensure correct WEBUI path.
# For simplicity, let's derive it based on the 'current' UI from settings.
UI_NAME = settings.get('current', 'Forge')
WEBUI_PATH = Path(settings.get('webui_path', str(HOME / UI_NAME))) # Use path from settings or derive

# Dictionary of WebUI zip URLs
UI_ZIPS = {
    "A1111": "https://huggingface.co/NagisaNao/ANXETY/resolve/main/A1111.zip",
    "Forge": "https://huggingface.co/NagisaNao/ANXETY/resolve/main/Forge.zip",
    "ReForge": "https://huggingface.co/NagisaNao/ANXETY/resolve/main/ReForge.zip",
    "Classic": "https://huggingface.co/NagisaNao/ANXETY/resolve/main/Classic.zip",
    "ComfyUI": "https://huggingface.co/NagisaNao/ANXETY/resolve/main/ComfyUI.zip",
    "SD-UX": "https://huggingface.co/NagisaNao/ANXETY/resolve/main/SD-UX.zip"
}

# --- System Dependency Management ---
def install_system_deps():
    """Checks for and installs essential system packages."""
    deps_check = {
        'aria2c': 'aria2',
        'lz4': 'lz4',
        'pv': 'pv',
        'ngrok': 'ngrok',
        'cloudflared': 'cloudflared'
    }
    
    missing_deps_names = []
    for cmd, pkg_name in deps_check.items():
        if not shutil.which(cmd):
            missing_deps_names.append(pkg_name)

    if not missing_deps_names:
        print("✅ All system dependencies are already installed.")
        return True
    
    print(f"🔧 Missing system dependencies: {', '.join(missing_deps_names)}. Attempting to install...")
    
    # Use subprocess.run for better control and error handling
    # For npm based tools, ensure npm is installed first
    try:
        # Update and install apt packages
        subprocess.run(["apt-get", "-y", "update", "-qq"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["apt-get", "-y", "install", "aria2", "lz4", "pv"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Install cloudflared
        if not shutil.which('cloudflared'):
            subprocess.run(shlex.split("wget -qO /usr/bin/cloudflared https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64"), check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["chmod", "+x", "/usr/bin/cloudflared"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # Install ngrok
        if not shutil.which('ngrok'):
            subprocess.run(shlex.split("wget -qO ngrok.tgz https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz"), check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(shlex.split("tar -xzf ngrok.tgz -C /usr/bin"), check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            Path('ngrok.tgz').unlink(missing_ok=True) # Clean up downloaded tgz

        print("✅ System dependency installation complete.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing system dependencies: {e.stderr.decode() if e.stderr else str(e)}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"❌ An unexpected error occurred during system dependency installation: {e}", file=sys.stderr)
        return False

def check_and_install_venv():
    """Manages virtual environment setup and reinstallation if needed."""
    current_ui = settings.get('current', 'Forge')
    is_classic_ui = (current_ui == 'Classic')

    # Determine required VENV type based on the selected UI (Classic needs Python 3.11)
    required_venv_type = 'Classic' if is_classic_ui else 'Standard'
    installed_venv_type = settings.get('venv_type')

    # Check if VENV exists and if it's the correct type
    if not VENV_PATH.exists() or installed_venv_type != required_venv_type:
        if VENV_PATH.exists():
            print("🗑️ VENV type has changed or VENV is corrupted. Removing old VENV...")
            shutil.rmtree(VENV_PATH)
            clear_output(wait=True) # Clear output after deletion message

        # Select appropriate VENV URL based on required type
        if required_venv_type == 'Classic':
            venv_url = "https://huggingface.co/NagisaNao/ANXETY/resolve/main/python31112-venv-torch251-cu121-C-Classic.tar.lz4"
            py_version_display = '(3.11.12)'
        else: # Standard VENV
            venv_url = "https://huggingface.co/NagisaNao/ANXETY/resolve/main/python31017-venv-torch251-cu121-C-fca.tar.lz4"
            py_version_display = '(3.10.17)'

        print(f"♻️ Installing VENV {py_version_display}. This will take some time...")
        
        filename = Path(urlparse(venv_url).path).name
        venv_archive_path = HOME / filename

        m_download(f'"{venv_url}" "{HOME}" "{filename}"', log=True)
        
        if not venv_archive_path.exists():
            print(f"❌ VENV DOWNLOAD FAILED for {filename}. Cannot proceed.", file=sys.stderr)
            sys.exit(1)

        print("📦 Unpacking VENV...")
        try:
            # Use subprocess.run for unpacking, as ipySys might be problematic in some contexts
            unpack_command = f"pv {shlex.quote(str(venv_archive_path))} | lz4 -d | tar xf -"
            subprocess.run(unpack_command, shell=True, check=True, cwd=HOME, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            venv_archive_path.unlink() # Clean up the archive
            js.save(str(SETTINGS_PATH), 'ENVIRONMENT.venv_type', required_venv_type) # Save the new VENV type
            print("✅ VENV setup complete.")
        except subprocess.CalledProcessError as e:
            print(f"❌ VENV UNPACKING FAILED: {e.stderr.decode() if e.stderr else str(e)}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"❌ An unexpected error occurred during VENV unpacking: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print("✨ Correct VENV already exists. Skipping VENV installation.")

# --- WebUI Installation ---
def install_webui():
    """Installs the selected WebUI if not already present."""
    global WEBUI_PATH # Use global to update in this scope
    UI_NAME = settings.get('current', 'Forge') # Get current UI from loaded settings
    WEBUI_PATH = Path(settings.get('webui_path', str(HOME / UI_NAME))) # Ensure WEBUI_PATH is consistent

    if not WEBUI_PATH.exists():
        print(f"📦 Unpacking Stable Diffusion | WEBUI: {UI_NAME}...")
        repo_url = UI_ZIPS.get(UI_NAME)

        if not repo_url:
            print(f"❌ No download URL defined for UI: {UI_NAME}. Cannot proceed.", file=sys.stderr)
            sys.exit(1)

        zip_path = HOME / f"{UI_NAME}.zip"
        
        m_download(f'"{repo_url}" "{HOME}" "{zip_path.name}"', log=True)
        
        if not zip_path.exists():
            print(f"❌ DOWNLOAD FAILED for {UI_NAME}.zip. Cannot proceed.", file=sys.stderr)
            sys.exit(1)
        
        print(f"🚚 Unzipping {UI_NAME} to {WEBUI_PATH}...")
        try:
            WEBUI_PATH.mkdir(parents=True, exist_ok=True) # Ensure target directory exists
            subprocess.run(['unzip', '-q', '-o', str(zip_path), '-d', str(WEBUI_PATH)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            zip_path.unlink() # Clean up zip file
            print(f"✅ {UI_NAME} installation complete!")
        except subprocess.CalledProcessError as e:
            print(f"❌ UNZIP FAILED for {UI_NAME}:\n{e.stderr.decode() if e.stderr else str(e)}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"❌ An unexpected error occurred during WebUI unpacking: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(f"✨ WebUI directory found for {UI_NAME}. Skipping installation.")

# --- Asset Downloading Logic ---
def read_data_file(file_path, data_key):
    """Reads data from a Python data file (e.g., _models-data.py)."""
    local_vars = {}
    if file_path.exists():
        try:
            with open(file_path, 'r', encoding="utf-8") as f:
                exec(f.read(), {}, local_vars)
        except Exception as e:
            print(f"❌ Error reading data file {file_path}: {e}", file=sys.stderr)
            return {}
    return local_vars.get(data_key, {})

def process_selections(selections, data_dict, prefix):
    """Generates download commands based on user selections and data dictionaries."""
    commands = []
    if not isinstance(selections, (list, tuple)): return commands

    # Adjust prefix map based on your Manager.py's PREFIX_MAP structure
    # For now, we'll assume it's just the prefix needed.
    
    for selection in selections:
        if selection == 'none' or not selection: continue
        
        model_name = selection # Assuming 'selection' is already the full model name as stored in data_dict keys
        
        if model_name in data_dict:
            model_data_value = data_dict[model_name]
            # Handle cases where data_dict value might be a list (e.g., for ControlNet) or a single dict
            model_info_list = model_data_value if isinstance(model_data_value, list) else [model_data_value]
            
            for model_info in model_info_list:
                if isinstance(model_info, dict) and 'url' in model_info:
                    # Construct filename carefully. prioritize 'name' field if present, otherwise parse from URL
                    file_name = model_info.get('name') or unquote(Path(urlparse(model_info['url']).path).name)
                    commands.append(f"{prefix}:{model_info['url']}[{file_name}]")
    return commands

def process_asset_downloads():
    """Orchestrates the downloading of user-selected models and assets."""
    print("\n--- Processing Asset Download Selections ---")

    # Access widget settings directly from the loaded `settings` dictionary
    is_xl = settings.get("sdxl_toggle", False) # Ensure 'sdxl_toggle' is saved in settings.json

    models_py_path = ANXETY_ROOT / 'scripts' / ('_xl-models-data.py' if is_xl else '_models-data.py')
    loras_py_path = ANXETY_ROOT / 'scripts' / '_loras-data.py'
    
    # Load model data
    model_data = read_data_file(models_py_path, 'sdxl_models_data' if is_xl else 'sd15_model_data')
    vae_data = read_data_file(models_py_path, 'sdxl_vae_data' if is_xl else 'sd15_vae_data')
    # For loras, get the nested dictionary based on SDXL/SD1.5
    lora_data_root = read_data_file(loras_py_path, 'lora_data')
    lora_data = lora_data_root.get('sdxl_loras' if is_xl else 'sd15_loras', {})
    controlnet_data = read_data_file(models_py_path, 'controlnet_list')

    all_download_commands = []
    
    # Process each type of selection
    all_download_commands.extend(process_selections(settings.get('model_list', []), model_data, 'model'))
    all_download_commands.extend(process_selections(settings.get('vae_list', []), vae_data, 'vae'))
    all_download_commands.extend(process_selections(settings.get('lora_list', []), lora_data, 'lora'))
    all_download_commands.extend(process_selections(settings.get('controlnet_list', []), controlnet_data, 'control'))

    # If 'empowerment' is on, process empowerment_output (direct URLs)
    if settings.get('empowerment', False) and settings.get('empowerment_output'):
        # This part requires a more direct parsing of empowerment_output as it's raw text
        # For simplicity, assuming a simple comma-separated list of URLs without prefixes for now.
        # This would need a more robust parser if empowerment_output can contain tags/prefixes.
        raw_urls = settings.get('empowerment_output').split(',')
        for url in raw_urls:
            url = url.strip()
            if url.startswith('http'):
                # Assuming basic file type guessing for raw URLs. This is simplified.
                guessed_type = "model" # Default guess
                if "lora" in url.lower(): guessed_type = "lora"
                elif "vae" in url.lower(): guessed_type = "vae"
                # Need to determine dst_dir dynamically or have a default
                # This requires access to webui_utils._set_webui_paths results.
                # For now, let's assume a generic download to model_dir if type is not recognized by a prefix.
                guessed_filename = unquote(Path(urlparse(url).path).name)
                all_download_commands.append(f"{guessed_type}:{url}[{guessed_filename}]")

    # If manual URLs were provided (Model_url, Vae_url, etc.)
    manual_url_fields = {
        'Model_url': 'model',
        'Vae_url': 'vae',
        'LoRA_url': 'lora',
        'Embedding_url': 'embed',
        'Extensions_url': 'extension',
        'ADetailer_url': 'adetailer',
        'custom_file_urls': 'file' # This one is special, might be a list of file paths/HTTP links to txt files
    }
    
    for field_name, prefix in manual_url_fields.items():
        if settings.get(field_name):
            # For simplicity, treat them as direct URLs with a guessed filename
            urls = settings.get(field_name).split(',')
            for url in urls:
                url = url.strip()
                if url.startswith('http'):
                    filename_match = re.search(r'\[(.*?)\]', url)
                    manual_filename = filename_match.group(1) if filename_match else unquote(Path(urlparse(url).path).name)
                    clean_url_for_dl = re.sub(r'\[.*?\]', '', url).strip() # Remove filename tag from URL for download
                    all_download_commands.append(f"{prefix}:{clean_url_for_dl}[{manual_filename}]")
                elif prefix == 'file': # Handle local file paths for custom_file_urls
                    # This would require reading the content of these local files
                    # and parsing them. This is complex and out of scope for a quick fix.
                    print(f"⚠️ Local file parsing for '{url}' not fully implemented here for {field_name}. Skipping.", file=sys.stderr)
                    pass


    if not all_download_commands:
        print("ℹ️ No assets were selected for download.")
    else:
        print(f"📦 Orchestrating downloads for {len(all_download_commands)} assets...")
        
        # Define the base directories for downloads, similar to webui_utils.py's path_config
        # These keys should match the 'prefix' used in process_selections
        path_map = {
            'model': settings.get('model_dir'),
            'vae': settings.get('vae_dir'),
            'lora': settings.get('lora_dir'),
            'embed': settings.get('embed_dir'),
            'extension': settings.get('extension_dir'),
            'adetailer': settings.get('adetailer_dir'),
            'control': settings.get('control_dir'),
            'upscale': settings.get('upscale_dir'),
            'clip': settings.get('clip_dir'),
            'unet': settings.get('unet_dir'),
            'vision': settings.get('vision_dir'),
            'encoder': settings.get('encoder_dir'),
            'diffusion': settings.get('diffusion_dir'),
            'config': settings.get('config_dir') # Usually configs are downloaded by UI scripts, not generic assets
        }

        # Detailed download mode should be read from settings.json
        detailed_download_on = settings.get('detailed_download') == 'on'

        for command_line in all_download_commands:
            try:
                # Expected format: "prefix:url[filename]"
                parts = command_line.split(':', 1)
                prefix = parts[0]
                url_and_filename = parts[1] # e.g., "https://example.com/model.safetensors[model.safetensors]"

                # Extract filename tag if present
                filename_match = re.search(r'\[(.*?)\]', url_and_filename)
                download_filename = filename_match.group(1) if filename_match else None
                
                # Extract URL, stripping the filename tag if present
                download_url = re.sub(r'\[.*?\]', '', url_and_filename).strip()

                dst_dir = path_map.get(prefix)

                if not dst_dir:
                    print(f"⚠️ Skipping download for {download_url}: No destination directory defined for prefix '{prefix}'.", file=sys.stderr)
                    continue

                if detailed_download_on:
                    print(f"⬇️ Queuing: {download_filename or download_url.split('/')[-1]} to {Path(dst_dir).name} (Type: {prefix})")
                
                # m_download expects url, dst_dir, filename
                m_download(f'"{download_url}" "{dst_dir}" "{download_filename or ""}"', log=detailed_download_on)

            except Exception as e:
                print(f"❌ Failed to process download command '{command_line}': {e}", file=sys.stderr)
        
        print("🏁 Download processing complete!")

# --- Main Execution for downloading-en.py ---
# This block is what gets executed when this script is run via %run from widgets_en.py.
if __name__ == '__main__':
    print("--- Starting Environment Setup & Asset Download ---")
    if not install_system_deps():
        sys.exit(1) # Exit if system dependencies fail
    
    check_and_install_venv()
    install_webui()
    process_asset_downloads()
    print("\n--- Environment Setup & Asset Download Complete ---")
