import subprocess
import threading

def runMP3(speech, word):
    speech.run(word)

def showImg(fileName, speech, word):
    try:
        thread = threading.Thread(target = runMP3, args = (speech, word))
        thread.start()
        subprocess.run(['feh', '-YF', fileName], timeout=3)
    except:
        print('openImg ended')
