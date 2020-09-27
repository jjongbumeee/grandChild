import subprocess
import threading
from buttonCamera import Camera

FILENAME = ''
def showImg():
    subprocess.run(['feh', '-YF', FILENAME], timeout=10)

def showim(fileName, speech, word):
    try:
        global FILENAME
        FILENAME = fileName
        imgThread = threading.Thread(target = showImg)
        imgThread.start()
        speech.run(word)
    except:
        print('openImg ended')
