import subprocess
import threading
import psutil

PROCNAME = "feh"
def runMP3(speech, word):
    speech.run(word)
def showim(fileName, speech, word):
    try:
        thread = threading.Thread(target = runMP3, args=(speech, word))
        thread.start()
        subprocess.run(['feh', '-YF', fileName], timeout=100)
    except:
        print('openImg ended')
def killImg():
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            proc.kill()
