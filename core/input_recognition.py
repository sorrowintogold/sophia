import os
from dotenv import load_dotenv
from elevenlabslib import set_api_key

class InputRecognition():
    def __init__(self) -> None:
        load_dotenv()
        set_api_key(
            os.getenv('ELEVENLABS_API_KEY')
        )
    
    def TTS(self, text: str):
        pass
    
    def STT(self, audio):
        pass