import os
import subprocess
import webbrowser

if __name__ == '__main__':
    subprocess.call('coverage run runner.py')
    subprocess.call('coverage html')
    webbrowser.open(f'file:///{os.getcwd()}/htmlcov/index.html')
