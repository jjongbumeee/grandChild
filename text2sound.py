import os
class Speech:
    def __init__(self):
        self.FILE_NAME = 'words.txt'
        self.AUDIO_NAME = 'output.mp3'
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'readingMachine.json'

    def synthesize_text(self, text):
        """Synthesizes speech from the input string of text."""
        from google.cloud import texttospeech

        client = texttospeech.TextToSpeechClient()

        input_text = texttospeech.SynthesisInput(text=text)

        # Note: the voice can also be specified by name.
        # Names of voices can be retrieved with client.list_voices().
        voice = texttospeech.VoiceSelectionParams(
            language_code="ko-KR",
            name="ko-KR-Wavenet-C",
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding = texttospeech.AudioEncoding.MP3,
            speaking_rate = 0.75
        )

        response = client.synthesize_speech(
            request={"input": input_text, "voice": voice, "audio_config": audio_config}
        )

        # The response's audio_content is binary.
        with open("output.mp3", "wb") as out:
            out.write(response.audio_content)


    def playsound(self, FILE_NAME):
        import subprocess
        # from playsound import playsound
        # playsound('output.mp3')
        subprocess.call(['omxplayer', '-o', 'local', './output.mp3'])
        os.remove(self.FILE_NAME)
        os.remove(self.AUDIO_NAME)
    
    def run(self, text):
        self.synthesize_text(text)
        self.playsound(self.FILE_NAME)