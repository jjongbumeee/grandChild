import subprocess
import threading
import psutil
from buttonCamera import Camera

PROCNAME = "feh"
def runMP3(speech, word):
    speech.run(word)
def showImg(fileName):
    subprocess.run(['feh', '-YF', fileName], timeout=100)

def showim(fileName, speech, word):
    try:
        # thread = threading.Thread(target = runMP3, args=(speech, word))
        # thread.start()
        imgThread = threading.Thread(target = showImg, args = (fileName))
        imgThread.start()
        speech.run(word)
    except:
        print('openImg ended')

def killImg():
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            proc.kill()
