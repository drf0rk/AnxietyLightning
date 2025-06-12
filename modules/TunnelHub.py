# /content/ANXETY/modules/TunnelHub.py (v2 - Heavy Debugging)

from typing import Callable, List, Optional, Tuple, TypedDict, Union, get_args
from threading import Event, Lock, Thread
from pathlib import Path
import subprocess
import logging
import socket
import shlex
import time
import re
import os

StrOrPath = Union[str, Path]
StrOrRegexPattern = Union[str, re.Pattern]
ListHandlersOrBool = Union[List[logging.Handler], bool]

class ColoredFormatter(logging.Formatter):
    COLORS = {'DEBUG': '\033[36m', 'INFO': '\033[32m', 'WARNING': '\033[33m', 'ERROR': '\033[31m', 'CRITICAL': '\033[31;1m'}
    def format(self, record):
        color = self.COLORS.get(record.levelno, '\033[0m')
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
        if not propagate:
            for handler in logger.handlers[:]: logger.removeHandler(handler)
        if not any(isinstance(h, logging.StreamHandler) for h in logger.handlers):
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logger.level)
            stream_handler.setFormatter(ColoredFormatter('{message}', style='{'))
            logger.addHandler(stream_handler)
        log_file = self.log_dir / 'tunnelhub.log'
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(FileFormatter("[%(asctime)s] [%(name)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"))
        logger.addHandler(file_handler)
        for handler in self.log_handlers: logger.addHandler(handler)
        return logger

    def is_command_available(self, command: str) -> bool:
        venv_bin_path = '/content/venv/bin'
        if os.access(os.path.join(venv_bin_path, command), os.X_OK):
            self.logger.debug(f"Command '{command}' found in VENV path: {venv_bin_path}")
            return True
        system_path = os.environ.get('PATH', '')
        for path in system_path.split(os.pathsep):
            if os.access(os.path.join(path, command), os.X_OK):
                self.logger.debug(f"Command '{command}' found in system PATH: {path}")
                return True
        self.logger.warning(f"Command '{command}' not found in VENV ('{venv_bin_path}') or system PATH.")
        return False

    def add_tunnel(self, *, command: str, pattern: StrOrRegexPattern, name: str, note: str = None, callback: Callable[[str, Optional[str], Optional[str]], None] = None) -> None:
        cmd_name = command.split()[0]
        if not self.is_command_available(cmd_name): return
        if isinstance(pattern, str): pattern = re.compile(pattern)
        self.logger.debug(f"Adding tunnel {command=} {pattern=} {name=} {note=} {callback=}")
        self.tunnel_list.append({'command': command, 'pattern': pattern, 'name': name, 'note': note, 'callback': callback})

    def start(self) -> None:
        if self._is_running: raise RuntimeError('Tunnel is already running')
        self.__enter__()
        try:
            while not self.printed.is_set(): time.sleep(1)
        except KeyboardInterrupt:
            self.logger.warning('\033[33m⚠️  Keyboard Interrupt detected, stopping tunnel\033[0m')
            self.stop()

    def stop(self) -> None:
        if not self._is_running: raise RuntimeError('Tunnel is not running')
        self.logger.info(f"💣 \033[32mTunnels:\033[0m \033[34m{self.get_tunnel_names()}\033[0m -> \033[31mKilled.\033[0m")
        self.stop_event.set()
        self.terminate_processes()
        self.join_threads()
        self.reset()

    def get_tunnel_names(self) -> str: return ', '.join(tunnel['name'] for tunnel in self.tunnel_list)

    def terminate_processes(self) -> None:
        for process in self.processes:
            try:
                if process.poll() is None: process.terminate(); process.wait(timeout=5)
            except Exception as e: self.logger.warning(f"Error terminating process: {str(e)}")
        self.processes.clear()

    def join_threads(self) -> None:
        for job in self.jobs: job.join()

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

    def __exit__(self, exc_type, exc_value, exc_tb): self.stop()

    def reset(self) -> None:
        self.urls.clear(); self.jobs.clear(); self.processes.clear()
        self.stop_event.clear(); self.printed.clear(); self._is_running = False

    @staticmethod
    def is_port_in_use(port: int) -> bool:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1); return s.connect_ex(('localhost', port)) == 0
        except Exception: return False

    @staticmethod
    def wait_for_condition(condition: Callable[[], bool], *, interval: int = 1, timeout: int = 10) -> bool:
        start_time = time.time(); elapsed_time = 0; checks_count = 0
        timeout = max(1, timeout) if timeout is not None else None
        while True:
            if condition(): return True
            checks_count += 1; elapsed_time = time.time() - start_time
            if timeout is not None and elapsed_time >= timeout: return False
            next_interval = min(interval, (timeout - elapsed_time) / (checks_count + 1)) if timeout else interval
            time.sleep(next_interval)

    def _process_line(self, line: str) -> bool:
        for tunnel in self.tunnel_list:
            if self.extract_url(tunnel, line): return True
        return False

    def extract_url(self, tunnel: TunnelDict, line: str) -> bool:
        regex = tunnel['pattern']; matches = regex.search(line)
        if matches:
            link = matches.group().strip()
            link = link if link.startswith('http') else 'http://' + link
            note, name, callback = tunnel.get('note'), tunnel.get('name'), tunnel.get('callback')
            with self.urls_lock: self.urls.append((link, note, name))
            if callback: self.invoke_callback(callback, link, note, name)
            return True
        return False

    def invoke_callback(self, callback: Callable, link: str, note: Optional[str], name: Optional[str]) -> None:
        try: callback(link, note, name)
        except Exception: self.logger.error('An error occurred while invoking URL callback', exc_info=True)

    def _run(self, cmd: str, name: str) -> None:
        log_path = self.log_dir / f"tunnel_{name}.log"; log_path.write_text('')
        log = self.logger.getChild(name); self.setup_file_logging(log, log_path)
        try:
            self.wait_for_port_if_needed()
            process = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, universal_newlines=True, bufsize=1)
            self.processes.append(process)
            self.monitor_process_output(process, log)
        except Exception as e: log.error(f"Error in tunnel: {str(e)}", exc_info=self.debug)
        finally:
            for handler in log.handlers: handler.close()

    def setup_file_logging(self, log: logging.Logger, log_path: Path) -> None:
        if not log.handlers:
            handler = logging.FileHandler(log_path, encoding='utf-8')
            handler.setLevel(logging.DEBUG)
            handler.setFormatter(FileFormatter("[%(name)s]: %(message)s"))
            log.addHandler(handler)

    def wait_for_port_if_needed(self) -> None:
        if self.check_local_port:
            self.wait_for_condition(lambda: self.is_port_in_use(self.port) or self.stop_event.is_set(), interval=1, timeout=None)

    def monitor_process_output(self, process: subprocess.Popen, log: logging.Logger) -> None:
        """Monitor the output of the subprocess and process any lines received."""
        url_extracted = False
        while not self.stop_event.is_set() and process.poll() is None:
            line = process.stdout.readline()
            if not line: break
            
            # --- NEW DEBUG LINE ---
            # This will print the raw output from the tunnel process to the main notebook cell
            print(f"[RAW_TUNNEL_OUTPUT:{log.name}] {line.strip()}")
            
            if not url_extracted:
                url_extracted = self._process_line(line)
            log.debug(line.rstrip())

    def _print(self) -> None:
        if self.check_local_port: self.wait_for_port_if_needed()
        if not self.wait_for_condition(lambda: len(self.urls) == len(self.tunnel_list) or self.stop_event.is_set(), interval=1, timeout=self.timeout):
            self.logger.warning('Timeout while getting tunnel URLs, print available URLs')
        if not self.stop_event.is_set(): self.display_urls()

    def display_urls(self) -> None:
        with self.urls_lock:
            width = 100
            tunnel_name_width = max(len(name) for _, _, name in self.urls) if self.urls else 6
            print('\n\033[32m+' + '=' * (width - 2) + '+\033[0m\n')
            for url, note, name in self.urls:
                print(f"\033[32m 🔗 Tunnel \033[0m{name:<{tunnel_name_width}}  \033[32mURL: \033[0m{url} {note or ''}")
            print('\n\033[32m+' + '=' * (width - 2) + '+\033[0m\n')
            if self.callback: self.invoke_callback(self.callback, self.urls)
            self.printed.set()
