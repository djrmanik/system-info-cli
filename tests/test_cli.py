import subprocess
import sys
import json

def run(cmd):
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    return p.returncode, p.stdout, p.stderr

def test_show_contains_system():
    code, out, err = run(f"{sys.executable} main.py show")
    assert code == 0
    assert "System:" in out

def test_json_output_is_valid():
    code, out, err = run(f"{sys.executable} main.py json")
    assert code == 0
    data = json.loads(out)
    assert "os_name" in data
    assert "cpu_count" in data
