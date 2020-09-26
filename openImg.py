import subprocess
import threading

def runMP3(speech, word):
    speech.run(word)
def showim(fileName, speech, word):
    try:
        thread = threading.Thread(target = runMP3, args=(i,))
        thread.start()
        subprocess.run(['feh', '-YF', fileName], timeout=100)
    except:
        print('openImg ended')
def killImg():
    #do process kill