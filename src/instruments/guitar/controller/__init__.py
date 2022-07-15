from instruments.guitar.inputs import *
import asyncio, time
class Guitar:
    def __init__(self, MicrophoneJack):
        self.input = MicrophoneJack
    
    def play(self):
          with self.input as stream:
              audio_generator = stream.generator()