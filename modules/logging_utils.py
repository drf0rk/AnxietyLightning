# /modules/logging_utils.py

import json
import logging
import sys
from pathlib import Path

def configure_logging(log_file_path):
    \"\"\"Configures a JSON logger.\"\"\"
    log_file_path = Path(log_file_path)
    log_file_path.parent.mkdir(parents=True, exist_ok=True)
    
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
        
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s', # We only want the raw JSON message
        handlers=[
            logging.FileHandler(log_file_path, mode='w', encoding='utf-8'),
            logging.StreamHandler(sys.stdout) # Also print to stdout
        ]
    )

def log(level, message, data=None):
    \"\"\"Logs a message in a structured JSON format.\"\"\"
    log_entry = {
        'level': level,
        'message': message,
        'data': data or {}
    }
    logger = logging.getLogger()
    
    json_message = json.dumps(log_entry, ensure_ascii=False)
    
    if level == 'error':
        logger.error(json_message)
    elif level == 'warning':
        logger.warning(json_message)
    else: # Default to info for 'success', 'progress', etc.
        logger.info(json_message)