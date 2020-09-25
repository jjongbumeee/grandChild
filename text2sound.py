import os
class Speech:
    def __init__(self):
        self.FILE_NAME = 'words.txt'
        self.AUDIO_NAME = 'output.mp3'
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'readingMachine.json'

    def synthesize_ssml(self, ssml):
        from google.cloud import texttospeech

        client = texttospeech.TextToSpeechClient()

        input_text = texttospeech.SynthesisInput(ssml=ssml)

        # Note: the voice can also be specified by name.
        # Names of voices can be retrieved with client.list_voices().
        voice = texttospeech.VoiceSelectionParams(
            language_code="ko-KR",
            name="ko-KR-Standard-C",
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        response = client.synthesize_speech(
            input=input_text, voice=voice, audio_config=audio_config
        )

        # The response's audio_content is binary.
        with open("output.mp3", "wb") as out:
            out.write(response.audio_content)

    def text_to_ssml(self, inputfile):
        import html
        # Generates SSML text from plaintext.
        # Given an input filename, this function converts the contents of the text
        # file into a string of formatted SSML text. This function formats the SSML
        # string so that, when synthesized, the synthetic audio will pause for two
        # seconds between each line of the text file. This function also handles
        # special text characters which might interfere with SSML commands.
        #
        # Args:
        # inputfile: string name of plaintext file
        #
        # Returns:
        # A string of SSML text based on plaintext input

        # Parses lines of input file
        with open(inputfile, "r") as f:
            raw_lines = f.read()

        # Replace special characters with HTML Ampersand Character Codes
        # These Codes prevent the API from confusing text with
        # SSML commands
        # For example, '<' --> '&lt;' and '&' --> '&amp;'

        escaped_lines = html.escape(raw_lines)

        # Convert plaintext to SSML
        # Wait two seconds between each address
        ssml = "<speak>{}</speak>".format(
            escaped_lines.replace("\n", '\n<break time="1s"/>')
        )

        # Return the concatenated string of ssml script
        return ssml

    def playsound(self, FILE_NAME):
        import subprocess
        from playsound import playsound
        playsound('output.mp3')
        # subprocess.call(['omxplayer', '-o', 'local', './output.mp3'])
        os.remove(self.FILE_NAME)
        os.remove(self.AUDIO_NAME)
    
    def run(self):
        self.synthesize_ssml(self.text_to_ssml(self.FILE_NAME))
        self.playsound(self.FILE_NAME)