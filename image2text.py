import io
import os
# Imports the Google Cloud client library
from google.cloud.vision import types

class Reader:
    def __init__(self, DIR_PATH, FILE_NAME):    
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'readingMachine.json'
        self.DIR_PATH = DIR_PATH
        self.FILE_NAME = FILE_NAME

    #이미지에 있는 글자를 출력
    def detect_text_uri(self):
        """Detects text in the file located in Google Cloud Storage or on the Web.
        """
        from google.cloud import vision
        client = vision.ImageAnnotatorClient()
        with io.open(os.path.join(self.DIR_PATH, self.FILE_NAME), 'rb') as image_file:
            content = image_file.read()
        image = vision.types.Image(content = content)
        #image.source.image_uri = uri

        response = client.text_detection(image=image)
        texts = response.text_annotations
        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))
        return texts[0].description

    def run(self):
        return self.detect_text_uri()
