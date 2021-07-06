import subprocess

def run(command):
    return subprocess.run(command, capture_output=True, text=True).stdout