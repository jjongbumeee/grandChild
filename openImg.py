import subprocess
import threading
import psutil
from buttonCamera import Camera

PROCNAME = "feh"
FILENAME = ''
def showImg():
    subprocess.run(['feh', '-YF', FILENAME], timeout=100)

def showim(fileName, speech, word):
    try:
        global FILENAME
        FILENAME = fileName
        imgThread = threading.Thread(target = showImg)
        imgThread.start()
        speech.run(word)
    except:
        print('openImg ended')

def killImg():
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            proc.kill()
