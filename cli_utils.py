import platform
import psutil
import shutil
import time
import os
import sys
from datetime import datetime

def collect_system_info():
    # OS info
    uname = platform.uname()
    os_name = platform.system()
    platform_str = platform.platform()
    kernel = uname.release

    # CPU
    cpu_count = psutil.cpu_count(logical=True)
    try:
        load1, load5, load15 = psutil.getloadavg()
        cpu_load = [round(load1, 2), round(load5, 2), round(load15, 2)]
    except (AttributeError, OSError):
        # Windows may not support getloadavg()
        cpu_load = [None, None, None]

    # Memory
    vm = psutil.virtual_memory()
    mem_total_mb = int(vm.total / 1024 / 1024)
    mem_used_mb = int(vm.used / 1024 / 1024)
    mem_free_mb = int(vm.available / 1024 / 1024)

    # Disk (root)
    du = shutil.disk_usage("/")
    disk_total_gb = round(du.total / 1024 / 1024 / 1024, 2)
    disk_used_gb = round(du.used / 1024 / 1024 / 1024, 2)
    disk_free_gb = round(du.free / 1024 / 1024 / 1024, 2)

    # Uptime
    try:
        boot_ts = psutil.boot_time()
        uptime_seconds = time.time() - boot_ts
    except Exception:
        uptime_seconds = 0

    info = {
        "os_name": os_name,
        "os_version": platform.version(),
        "platform": platform_str,
        "kernel": kernel,
        "cpu_count": cpu_count,
        "cpu_load": cpu_load,
        "mem_total_mb": mem_total_mb,
        "mem_used_mb": mem_used_mb,
        "mem_free_mb": mem_free_mb,
        "disk_total_gb": disk_total_gb,
        "disk_used_gb": disk_used_gb,
        "disk_free_gb": disk_free_gb,
        "uptime_seconds": uptime_seconds,
        "python_version": platform.python_version(),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

    # add env info
    info["env"] = {
        "user": os.getenv("USER") or os.getenv("USERNAME") or "",
        "cwd": os.getcwd()
    }

    return info
