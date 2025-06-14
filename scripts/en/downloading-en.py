# /content/ANXETY/scripts/en/downloading-en.py (v18 - Add Unzip Dependency)
# ... (rest of the file is the same)
def install_system_deps():
    log('header', 'Checking and Installing System Dependencies...')
    try:
        subprocess.run(["apt-get", "update", "-y", "-qq"], check=True, capture_output=True)
        # Add 'unzip' to the list of essential packages
        subprocess.run(["apt-get", "install", "-y", "-qq"] + ['aria2', 'lz4', 'unzip'], check=True, capture_output=True)
        return True
    except: 
        log('error', "Failed to install system dependencies via apt-get.")
        return False
# ... (rest of the file is the same)