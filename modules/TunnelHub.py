# /content/ANXETY/modules/TunnelHub.py (v5 - Final Fix)

from typing import Callable, List, Optional, Tuple, TypedDict, Union
from threading import Event, Lock, Thread
from pathlib import Path
import subprocess
import logging
import socket
import shlex
import time
import re
import os
import shutil

StrOrPath = Union[str, Path]
StrOrRegexPattern = Union[str, re.Pattern]
ListHandlersOrBool = Union[List[logging.Handler], bool]

class ColoredFormatter(logging.Formatter):
    COLORS = {'DEBUG': '\033[36m', 'INFO': '\033[32m', 'WARNING': '\033[33m', 'ERROR': '\033[31m', 'CRITICAL': '\033[31;1m'}
    def format(self, record):
        color = self.COLORS.get(logging.getLevelName(record.levelno), '\033[0m')
        message = super().format(record)
        return f"\n{color}[{record.name}]:\033[0m {message}"

class FileFormatter(logging.Formatter):
    @staticmethod
    def strip_ansi_codes(text: str) -> str:
        return re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])').sub('', text)
    def format(self, record):
        return self.strip_ansi_codes(super().format(record))

class TunnelDict(TypedDict):
    command: str; pattern: re.Pattern; name: str; note: Optional[str]
    callback: Optional[Callable[[str, Optional[str], Optional[str]], None]]

class Tunnel:
    def __init__( self, port: int, check_local_port: bool = True, debug: bool = False, timeout: int = 15, propagate: bool = False, log_handlers: ListHandlersOrBool = None, log_dir: StrOrPath = None, callback: Callable[[List[Tuple[str, Optional[str]]]], None] = None):
        self._is_running = False
        self.urls: List[Tuple[str, Optional[str], Optional[str]]] = []
        self.urls_lock = Lock()
        self.jobs: List[Thread] = []
        self.processes: List[subprocess.Popen] = []
        self.tunnel_list: List[TunnelDict] = []
        self.stop_event: Event = Event()
        self.printed = Event()
        self.port = port
        self.check_local_port = check_local_port
        self.debug = debug
        self.timeout = timeout
        self.log_handlers = log_handlers or []
        self.log_dir = Path(log_dir) if log_dir else Path.home() / 'tunnel_logs'
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.callback = callback
        self.logger = self.setup_logger(propagate)

    def setup_logger(self, propagate: bool) -> logging.Logger:
        logger = logging.getLogger('TunnelHub')
        logger.setLevel(logging.DEBUG if self.debug else logging.INFO)
        logger.propagate = propagate
        if not propagate and logger.hasHandlers():
            for handler in logger.handlers[:]: logger.removeHandler(handler)
        if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
            stream_handler = logging.StreamHandler(); stream_handler.setLevel(logger.level)
            stream_handler.setFormatter(ColoredFormatter('{message}', style='{')); logger.addHandler(stream_handler)
        log_file = self.log_dir / 'tunnelhub.log'
        file_handler = logging.FileHandler(log_file, encoding='utf-8', mode='a')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(FileFormatter("[%(asctime)s] [%(name)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")); logger.addHandler(file_handler)
        for handler in self.log_handlers: logger.addHandler(handler)
        return logger

    def is_command_available(self, command: str) -> bool: return shutil.which(command) is not None

    def add_tunnel(self, *, command: str, pattern: StrOrRegexPattern, name: str, note: str = None, callback: Callable[[str, Optional[str], Optional[str]], None] = None) -> None:
        cmd_name = shlex.split(command)[0]
        if not self.is_command_available(cmd_name): self.logger.warning(f"Command '{cmd_name}' not found. Skipping tunnel '{name}'."); return
        if isinstance(pattern, str): pattern = re.compile(pattern)
        self.logger.debug(f"Adding tunnel {command=} {pattern=} {name=} {note=} {callback=}")
        self.tunnel_list.append({'command': command, 'pattern': pattern, 'name': name, 'note': note, 'callback': callback})

    def __enter__(self):
        if self._is_running: raise RuntimeError('Tunnel is already running by another method')
        if not self.tunnel_list: raise ValueError('No tunnels added')
        print_job = Thread(target=self._print); print_job.start(); self.jobs.append(print_job)
        for tunnel in self.tunnel_list: self.start_tunnel_thread(tunnel)
        self._is_running = True
        return self
        
    def start_tunnel_thread(self, tunnel: TunnelDict) -> None:
        try:
            cmd = tunnel['command'].format(port=self.port); name = tunnel.get('name')
            tunnel_thread = Thread(target=self._run, args=(cmd, name)); tunnel_thread.start(); self.jobs.append(tunnel_thread)
        except Exception as e: self.logger.error(f"Failed to start tunnel {tunnel.get('name')}: {str(e)}")

    def _run(self, cmd: str, name: str) -> None:
        log = self.logger.getChild(name)
        log.debug(f"Process starting with command: {cmd}")
        try:
            self.wait_for_port_if_needed()
            process = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8', errors='replace')
            self.processes.append(process)
            for line in iter(process.stdout.readline, ''):
                if self.stop_event.is_set(): break
                log.debug(line.strip())
                self._process_line(line)
            process.stdout.close()
            return_code = process.wait()
            log.debug(f"Process finished with exit code {return_code}")
        except Exception as e:
            log.error(f"Error in tunnel process: {str(e)}", exc_info=self.debug)

    def _print(self) -> None:
        if self.check_local_port: self.wait_for_port_if_needed()
        if not self.wait_for_condition(lambda: len(self.urls) >= 1 or self.stop_event.is_set(), timeout=self.timeout):
             self.logger.warning('Timeout while getting tunnel URLs. Check debug output for errors.')
        if not self.stop_event.is_set() and self.urls: self.display_urls()
        self.printed.set()

    def display_urls(self) -> None:
        with self.urls_lock:
            if not self.urls: return
            print('\n\033[32m+' + '='*98 + '+\033[0m\n')
            for url, note, name in self.urls:
                print(f"\033[32m 🔗 Tunnel \033[0m{name:<10}  \033[32mURL: \033[0m{url} {note or ''}")
            print('\n\033[32m+' + '='*98 + '+\033[0m\n')
            if self.callback: self.invoke_callback(self.callback, self.urls)
            self.printed.set()

    # --- THIS IS THE CORRECTED FUNCTION ---
    @staticmethod
    def wait_for_condition(condition: Callable[[], bool], *, interval: int = 1, timeout: int = 10) -> bool:
        start_time = time.time()
        while True:
            if condition(): return True
            if timeout is not None and time.time() - start_time >= timeout: return False
            time.sleep(interval)
            
    def wait_for_port_if_needed(self) -> None:
        if self.check_local_port:
            print(f"DEBUG: Waiting for port {self.port} to be in use...")
            if self.wait_for_condition(lambda: self.is_port_in_use(self.port) or self.stop_event.is_set(), timeout=120):
                 print(f"DEBUG: Port {self.port} is now active.")
            else:
                 print(f"WARNING: Timed out waiting for port {self.port}.")

    @staticmethod
    def is_port_in_use(port: int) -> bool:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: s.settimeout(1); return s.connect_ex(('localhost', port)) == 0
        except Exception: return False
        
    def _process_line(self, line:str)->bool:
        for tunnel in self.tunnel_list:
            if self.extract_url(tunnel,line): return True
        return False
        
    def extract_url(self, tunnel:TunnelDict, line:str)->bool:
        match = tunnel['pattern'].search(line)
        if match:
            url = match.group().strip()
            url = url if url.startswith('http') else 'http://' + url
            with self.urls_lock:
                # Avoid adding duplicate URLs
                if not any(u[0] == url for u in self.urls):
                    self.urls.append((url, tunnel.get('note'), tunnel.get('name')))
                    print(f"\n--- ✅ DETECTED PUBLIC URL: {url} --- \n")
            return True
        return False
        
    def stop(self) -> None: self.stop_event.set(); self.terminate_processes(); self.join_threads(); self.reset()
    def terminate_processes(self) -> None:
        for p in self.processes:
            if p.poll() is None: p.terminate()
    def join_threads(self) -> None:
        for j in self.jobs: j.join(timeout=2)
    def reset(self) -> None: self._is_running=False; self.urls.clear(); self.jobs.clear(); self.processes.clear(); self.stop_event.clear(); self.printed.clear()
    def invoke_callback(self,c,u,n,a):
        try:c(u,n,a)
        except Exception:self.logger.error('Error in URL callback',exc_info=True)
