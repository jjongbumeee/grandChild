from PIL import Image, ImageDraw, ImageFont
from image2text import Reader
from text2sound import Speech
import subprocess
from os import remove
from buttonCamera import Camera
import openImg

DIR_PATH = './resources'
FILE_NAME = 'test.jpg'
camera = Camera(DIR_PATH, FILE_NAME)
reader = Reader(DIR_PATH, FILE_NAME)
speech = Speech()
while True:
    camera.run()
    words = reader.run().split('\n')[:-1]
    for i in range(len(words)):
        word = words[i]
        print(word)
        img = Image.new('RGB', (len(word) * 45, 80), color = (0, 0, 0))
        d = ImageDraw.Draw(img)
        fnt = ImageFont.truetype('./Font.ttf', 50)
        d.text((10, 10), word, font = fnt, fill = (255, 255, 255))
        FILE_NAME = 'test{}.png'.format(i)
        img.save(FILE_NAME)
        # subprocess.call(['open', FILE_NAME])
        openImg.showim('test{}.png'.format(i), speech, word)
        speech.run(word)
        camera.getBtn().wait_for_press()
        openImg.killImg()

    for i in range(len(words)):
        remove('test{}.png'.format(i))
