import pyaudio
import numpy as np
from instruments.guitar.settings import *
from instruments.guitar.effects import GEcore

class MicrophoneJack:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.frames= []

    def open_live_audio_stream(self):
        self.stream = self.audio.open(format=self.audio.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK)

    def capture_audio_data(self, export = False):
        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = self.stream.read(CHUNK)
            self.stream.write(data, CHUNK)
            if export:
                self.frames.append(data)
    
    def close_stream(self):
        self.stream.stop_stream()
        self.stream.close()
    
    def terminate_audio(self):
        self.audio.terminate()