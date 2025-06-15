# /scripts/_logic.py

import os
import sys
from pathlib import Path
import subprocess
import html
import json
import time

# --- Environment Setup ---
ANXETY_ROOT = Path(os.environ.get("ANXETY_ROOT", "/content/ANXETY"))
HOME_DIR = Path(os.environ.get("HOME_DIR", "/content"))
NGROK_TOKEN_ENV = os.environ.get("NGROK_TOKEN", "")

# We must ensure modules can be imported
if str(ANXETY_ROOT) not in sys.path:
    sys.path.insert(0, str(ANXETY_ROOT))

try:
    from modules import json_utils as js
    from modules import webui_utils
except ImportError as e:
    print(f"❌ CRITICAL [Logic]: Failed to import core modules. Error: {e}")
    sys.exit(1)


# --- Configuration ---
webui_selection_args = {
    'A1111': "--xformers --no-half-vae --skip-torch-cuda-test --reinstall-xformers",
    'Forge': "--disable-xformers --opt-sdp-attention --cuda-stream --pin-shared-memory --skip-torch-cuda-test",
    'ReForge': "--disable-xformers --cuda-stream --pin-shared-memory --skip-torch-cuda-test",
    'Classic': "--persistent-patches --cuda-stream --skip-torch-cuda-test --reinstall-xformers",
    'ComfyUI': "--use-sage-attention",
    'SD-UX': "--xformers --no-half-vae --skip-torch-cuda-test --reinstall-xformers"
}


# --- Core Logic Functions ---

def _serialize_settings_to_json(webui_choice, is_sdxl, selected_models, selected_vaes, selected_loras, selected_cnets, launch_args, ngrok_token_val, detailed_download):
    """Saves all user selections from the UI into settings.json."""
    final_launch_args = launch_args
    default_args_for_ui = webui_selection_args.get(webui_choice, "")

    if not final_launch_args:
        final_launch_args = default_args_for_ui
    else:
        default_flags = default_args_for_ui.split()
        user_flags = final_launch_args.split()
        for flag in default_flags:
            if flag not in user_flags:
                if flag == '--disable-xformers' and '--xformers' in user_flags: continue
                if flag == '--xformers' and '--disable-xformers' in user_flags: continue
                final_launch_args += f" {flag}"

    final_launch_args = ' '.join(list(dict.fromkeys(final_launch_args.split())))

    settings_data = {
        'WIDGETS': {
            'change_webui': webui_choice, 'sdxl_toggle': is_sdxl,
            'model_list': selected_models or [], 'vae_list': selected_vaes or [],
            'lora_list': selected_loras or [], 'controlnet_list': selected_cnets or [],
            'commandline_arguments': final_launch_args,
            'ngrok_token': ngrok_token_val or NGROK_TOKEN_ENV,
            'detailed_download': detailed_download
        },
        'ENVIRONMENT': {'home_path': str(HOME_DIR)}
    }
    settings_path = ANXETY_ROOT / 'settings.json'
    js.save(str(settings_path), 'WIDGETS', settings_data['WIDGETS'])
    js.save(str(settings_path), 'ENVIRONMENT', settings_data['ENVIRONMENT'])
    webui_utils.update_current_webui(webui_choice)

def format_log_line(line):
    """Formats a raw log line into styled HTML for the Gradio UI."""
    clean_line = line.strip()
    if not clean_line: return None, False

    try:
        log_entry = json.loads(clean_line)
        level = log_entry.get('level', 'info')
        message = html.escape(log_entry.get('message', ''))
        
        if level == 'progress':
            raw_data = html.escape(log_entry.get('data', {}).get('raw_line', ''))
            percent = log_entry.get('data', {}).get('percentage', 0)
            formatted_message = f"🔄 {message} ({percent}%) {raw_data}"
            return f'<span class="log-line log-download progress-line">{formatted_message}</span>', True

        return f'<span class="log-line log-{level}">{message}</span>', False

    except json.JSONDecodeError:
        escaped_line = html.escape(clean_line)
        if '%' in escaped_line and ('MiB/s' in escaped_line or 'ETA' in escaped_line):
            return f'<span class="log-line log-download progress-line">🔄 {escaped_line}</span>', True
        elif any(x in escaped_line for x in ["gradio.live", ".trycloudflare.com", "ngrok-free.app"]):
            return f'<span class="log-line log-url">🔗 {escaped_line}</span>', False
        else:
            return f'<span class="log-line">{escaped_line}</span>', False

def save_and_launch_generator(webui_choice, is_sdxl, selected_models, selected_vaes, selected_loras, selected_cnets, launch_args, ngrok_token_val, detailed_download):
    """The main generator function called by the Gradio UI."""
    _serialize_settings_to_json(webui_choice, is_sdxl, selected_models, selected_vaes, selected_loras, selected_cnets, launch_args, ngrok_token_val, detailed_download)
    log_lines_list = ['<span class="log-line log-success">✅ Settings saved. Orchestrator starting backend setup...</span>']
    yield "".join(log_lines_list)
    time.sleep(0.5)

    scripts_to_run = [ANXETY_ROOT / 'scripts' / 'en' / 'downloading-en.py', ANXETY_ROOT / 'scripts' / 'launch.py']

    for script_path in scripts_to_run:
        log_lines_list.append(f'<span class="log-line log-header">--- 🚀 Running {script_path.name} ---</span>')
        yield "".join(log_lines_list)

        try:
            process = subprocess.Popen([sys.executable, str(script_path)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace', bufsize=1)

            for line in iter(process.stdout.readline, ''):
                html_line, is_progress = format_log_line(line)
                if html_line:
                    last_was_progress = 'progress-line' in (log_lines_list[-1] if log_lines_list else "")

                    if is_progress and last_was_progress:
                        log_lines_list[-1] = html_line
                    elif '✅✅✅' in html_line and last_was_progress:
                        log_lines_list.pop()
                        log_lines_list.append(html_line)
                    else:
                        log_lines_list.append(html_line)

                    if len(log_lines_list) > 500:
                        log_lines_list = log_lines_list[-400:]

                    yield "".join(log_lines_list)

            process.wait()
            if process.returncode != 0:
                error_message = f'<span class="log-line log-error">--- ❌ {script_path.name} failed with exit code {process.returncode}. Halting. ---</span>'
                log_lines_list.append(error_message)
                yield "".join(log_lines_list)
                break

        except Exception as e:
            error_message = f'<span class="log-line log-error">--- ❌ CRITICAL FAILURE ({script_path.name}): {html.escape(str(e))} ---</span>'
            log_lines_list.append(error_message)
            yield "".join(log_lines_list)
            break

    if 'process' in locals() and process.returncode == 0:
        success_message = '<span class="log-line log-success">--- ✅ Process Complete or Terminated Successfully ---</span>'
        log_lines_list.append(success_message)
        yield "".join(log_lines_list)