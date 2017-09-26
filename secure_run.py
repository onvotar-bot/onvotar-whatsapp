import sys
import time
import subprocess


def secure_run():
    p = subprocess.Popen(['python3', 'run.py'])
    while True:
        time.sleep(5)
        if p.poll() is not None:
            print('!!!!!!!!!!!!!!!!!!!!!!!!')
            print('RECOVERING FROM DISASTER')
            print('!!!!!!!!!!!!!!!!!!!!!!!!')
            break
    secure_run()

try:
    secure_run()
except KeyboardInterrupt:
    sys.exit(0)
