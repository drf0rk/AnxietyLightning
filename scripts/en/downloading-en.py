# /content/ANXETY/scripts/en/downloading-en.py (FINAL - WITH VENV LOGIC)

import os
import sys
from pathlib import Path
import subprocess
import re
from urllib.parse import urlparse
import shlex
import shutil

# --- Self-aware pathing ---
try:
    ANXETY_ROOT = Path(__file__).resolve().parents[2]
except NameError:
    ANXETY_ROOT = Path.cwd()

# Ensure modules can be imported
if str(ANXETY_ROOT) not in sys.path: sys.path.insert(0, str(ANXETY_ROOT))
if str(ANXETY_ROOT / 'modules') not in sys.path: sys.path.insert(0, str(ANXETY_ROOT / 'modules'))

import modules.json_utils as js
from modules.Manager import m_download

# --- Constants ---
SETTINGS_PATH = ANXETY_ROOT / 'settings.json'
SCRIPTS_UIs = ANXETY_ROOT / 'scripts' / 'UIs'
WEBUI_DIR_MAPPING = {'A1111': 'A1111', 'Forge': 'Forge', 'ReForge': 'ReForge', 'Classic': 'Classic', 'ComfyUI': 'ComfyUI', 'SD-UX': 'SD-UX'}
HOME = Path(js.read(SETTINGS_PATH, 'ENVIRONMENT.home_path', str(Path.home())))
VENV_PATH = HOME / 'venv'

# --- VENV and System Dependency Management ---

def install_system_deps():
    """Installs required system-level packages like aria2 and lz4."""
    if js.key_exists(SETTINGS_PATH, 'ENVIRONMENT.system_deps_installed'):
        print("✅ System dependencies already installed.")
        return

    print("🔧 Installing required system dependencies (aria2, lz4, etc.)...")
    commands = {
        'aria2': "apt-get -y install -qq aria2",
        'lz4': "apt-get -y install -qq lz4",
        'pv': "apt-get -y install -qq pv"
    }
    env = os.environ.copy()
    env['DEBIAN_FRONTEND'] = 'noninteractive'

    for pkg, cmd in commands.items():
        try:
            subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True, env=env)
        except Exception as e:
            print(f"  - ❌ Warning: Failed to install system package '{pkg}'. This may cause issues if not already present. Error: {e}", file=sys.stderr)
            
    js.save(str(SETTINGS_PATH), 'ENVIRONMENT.system_deps_installed', True)
    print("✅ System dependency check complete.")

def setup_venv(url, py_version):
    """Downloads and unpacks the correct pre-packaged Virtual Environment."""
    print(f"♻️ Installing VENV {py_version}, this will take some time...")
    filename = Path(urlparse(url).path).name
    venv_archive_path = HOME / filename
    
    m_download(f'"{url}" "{HOME}" "{filename}"', log=True)
    
    if not venv_archive_path.exists():
        print(f"❌ VENV DOWNLOAD FAILED for {filename}. Cannot proceed.", file=sys.stderr)
        sys.exit(1)

    print("  - Unpacking VENV...")
    unpack_command = f"pv {venv_archive_path} | lz4 -d | tar xf -"
    subprocess.run(unpack_command, shell=True, check=True, cwd=HOME)
    venv_archive_path.unlink()
    
    print("✅ VENV setup complete.")

def check_and_install_venv():
    """Checks if the correct VENV exists and installs it if necessary."""
    current_ui = js.read(SETTINGS_PATH, 'WEBUI.current')
    if not current_ui:
        print("❌ Cannot determine current UI. VENV check aborted.", file=sys.stderr)
        return

    is_classic_ui = current_ui == 'Classic'
    venv_type_key = 'venv_type'
    
    required_venv_type = 'Classic' if is_classic_ui else 'Standard'
    installed_venv_type = js.read(SETTINGS_PATH, f'ENVIRONMENT.{venv_type_key}')

    if not VENV_PATH.exists() or installed_venv_type != required_venv_type:
        if VENV_PATH.exists():
            print("🗑️ VENV type has changed. Removing old VENV...")
            shutil.rmtree(VENV_PATH)
        
        if is_classic_ui:
            venv_url = "https://huggingface.co/NagisaNao/ANXETY/resolve/main/python31112-venv-torch251-cu121-C-Classic.tar.lz4"
            py_version = '(3.11.12)'
        else:
            venv_url = "https://huggingface.co/NagisaNao/ANXETY/resolve/main/python31017-venv-torch251-cu121-C-fca.tar.lz4"
            py_version = '(3.10.17)'
            
        setup_venv(venv_url, py_version)
        js.save(str(SETTINGS_PATH), f'ENVIRONMENT.{venv_type_key}', required_venv_type)
    else:
        print("✅ Correct VENV already exists. Skipping installation.")

# --- The rest of the script for model downloading ---

def get_webui_path():
    webui_settings = js.read(SETTINGS_PATH, 'WEBUI', {})
    return Path(webui_settings['webui_path']) if webui_settings.get('webui_path') else None, webui_settings.get('current')

def read_data_file(file_path, data_key):
    local_vars = {}
    if file_path.exists():
        with open(file_path, 'r', encoding='utf-8') as f: exec(f.read(), {}, local_vars)
    return local_vars.get(data_key, {})

def process_selections(selections, data_dict, prefix):
    commands = []
    if not isinstance(selections, (list, tuple)): return commands
    for selection in selections:
        if selection == 'none' or not selection: continue
        if selection == 'ALL':
            for model_name, model_data_value in data_dict.items():
                model_info_list = model_data_value if isinstance(model_data_value, list) else [model_data_value]
                for model_info in model_info_list:
                    if isinstance(model_info, dict): commands.append(f"{prefix}:{model_info['url']}[{model_info.get('name', '')}]")
            continue
        model_name = selection.split('. ', 1)[-1]
        if model_name in data_dict:
            model_data_value = data_dict[model_name]
            model_info_list = model_data_value if isinstance(model_data_value, list) else [model_data_value]
            for model_info in model_info_list:
                if isinstance(model_info, dict): commands.append(f"{prefix}:{model_info['url']}[{model_info.get('name', '')}]")
    return commands

def main():
    install_system_deps()
    check_and_install_venv()

    print(f"✅ Running download orchestrator: {__file__}")
    settings = js.read(SETTINGS_PATH, 'WIDGETS', {})
    webui_paths = js.read(SETTINGS_PATH, 'WEBUI', {})
    if not settings or not webui_paths:
        print("❌ Critical settings missing. Cannot proceed."); return

    WEBUI_PATH, webui_name = get_webui_path()
    if not WEBUI_PATH or not webui_name:
        print("❌ Halting due to missing WebUI configuration."); return

    if not WEBUI_PATH.exists():
        print(f"🚀 Unpacking Stable Diffusion | WEBUI: {webui_name}...")
        installer_script = SCRIPTS_UIs / f"{WEBUI_DIR_MAPPING.get(webui_name, webui_name)}.py"
        if installer_script.exists():
            try:
                subprocess.run([sys.executable, str(installer_script)], check=True, capture_output=True, text=True)
            except subprocess.CalledProcessError as e:
                print("\n" + "="*80); print(f"❌❌❌ WEBUI INSTALLER SCRIPT FAILED! ('{installer_script.name}') ❌❌❌"); print("--- Captured Stderr ---\n", e.stderr); print("="*80 + "\n"); raise e
        else:
            print(f"❌ Installer script not found: {installer_script}"); return
    else:
        print(f"🔧 WebUI found: {webui_name}")

    print("📦 Processing asset download selections...")
    is_xl = settings.get('XL_models', False)
    models_py_path = ANXETY_ROOT / 'scripts' / ('_xl-models-data.py' if is_xl else '_models-data.py')
    loras_py_path = ANXETY_ROOT / 'scripts' / '_loras-data.py'
    
    model_data = read_data_file(models_py_path, 'sdxl_models_data' if is_xl else 'sd15_model_data')
    vae_data = read_data_file(models_py_path, 'sdxl_vae_data' if is_xl else 'sd15_vae_data')
    lora_data = read_data_file(loras_py_path, 'lora_data').get('sdxl_loras' if is_xl else 'sd15_loras', {})
    cnet_data = read_data_file(models_py_path, 'controlnet_list')

    all_commands = []
    all_commands.extend(process_selections(settings.get('model', []), model_data, 'model'))
    all_commands.extend(process_selections(settings.get('vae', []), vae_data, 'vae'))
    all_commands.extend(process_selections(settings.get('lora', []), lora_data, 'lora'))
    all_commands.extend(process_selections(settings.get('controlnet', []), cnet_data, 'control'))

    if not all_commands:
        print("⏩ No assets were selected for download.")
    else:
        print(f"▶️  Orchestrating downloads for {len(all_commands)} assets...")
        PREFIX_PATH_MAP = { 'model': webui_paths.get('model_dir'), 'vae': webui_paths.get('vae_dir'), 'lora': webui_paths.get('lora_dir'), 'control': webui_paths.get('control_dir') }

        for command in all_commands:
            try:
                prefix, rest = command.split(':', 1)
                if prefix not in PREFIX_PATH_MAP: continue
                url_match = re.match(r"(.*?)(?:\[(.*?)\])?$", rest)
                url, filename = url_match.groups()
                if not filename: filename = Path(urlparse(url).path).name
                dst_dir = PREFIX_PATH_MAP[prefix]
                if not dst_dir: continue
                final_command = f'"{url}" "{dst_dir}" "{filename}"'
                print(f"  - 🔽 Queuing: {filename} to {dst_dir}")
                m_download(final_command, log=True, unzip=True)
            except Exception as e:
                print(f"  - ❌ Failed to process command '{command}': {e}")
                
    print("🏁 Download processing complete!")

if __name__ == '__main__':
    main()
