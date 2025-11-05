#!/usr/bin/env python3
"""
System Info CLI
Usage:
  python main.py show        # human readable
  python main.py json        # JSON output
  python main.py save file   # save JSON to file
"""
import argparse
import json
from cli_utils import collect_system_info

def main():
    parser = argparse.ArgumentParser(prog="system-info", description="Simple System Info CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("show", help="Show system info (human readable)")
    sub.add_parser("json", help="Show system info as JSON")
    save_parser = sub.add_parser("save", help="Save JSON system info to file")
    save_parser.add_argument("file", help="Output filename (e.g. info.json)")

    args = parser.parse_args()
    info = collect_system_info()

    if args.cmd == "show":
        # Pretty print
        print("=== System Info ===")
        print(f"System: {info['os_name']} {info['os_version']}")
        print(f"Platform: {info['platform']}")
        print(f"Kernel: {info['kernel']}")
        print(f"CPU cores (logical): {info['cpu_count']}")
        print(f"CPU load (1m,5m,15m): {', '.join(map(str, info['cpu_load']))}")
        print(f"Memory (total, used, free) MB: {info['mem_total_mb']}, {info['mem_used_mb']}, {info['mem_free_mb']}")
        print(f"Disk / (total, used, free) GB: {info['disk_total_gb']}, {info['disk_used_gb']}, {info['disk_free_gb']}")
        print(f"Uptime (seconds): {info['uptime_seconds']:.0f}")
        print(f"Python: {info['python_version']}")
    elif args.cmd == "json":
        print(json.dumps(info, indent=2))
    elif args.cmd == "save":
        with open(args.file, "w") as f:
            json.dump(info, f, indent=2)
        print(f"Wrote JSON to {args.file}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
