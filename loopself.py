import subprocess
import os
import sys

while True:
    if os.path.isfile('quit.txt'):
        kill = open('quit.txt').read()
        os.remove('quit.txt')
        if kill == 'update':
            exit(15)
        break
    params = [sys.executable, 'appuselfbot.py']
    for arg in sys.argv[1:]:
        params.append(arg)
    subprocess.call(params)
