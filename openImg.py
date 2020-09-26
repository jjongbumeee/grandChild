import subprocess
try:
    subprocess.run(['feh', '-YF', 'resources/test.jpg'], timeout=3)
except:
    print('openImg ended')
