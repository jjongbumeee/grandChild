from image2text import Reader
from text2sound import Speech
from buttonCamera import Camera
DIR_PATH = './resources'
FILE_NAME = 'test.jpg'
camera = Camera(DIR_PATH, FILE_NAME)
camera.run()
reader = Reader(DIR_PATH, FILE_NAME)
speech = Speech()
reader.run()
speech.run()
