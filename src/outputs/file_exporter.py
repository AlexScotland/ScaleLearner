from instruments.guitar.settings import *
import pyaudio
import wave
class ExportAudio:
    def __init__(self):
        self.audio = None# Open and Set the data of the WAV file
    
    def export_audio(self, instrument, file_name):
        file = wave.open(file_name, 'wb')
        file.setnchannels(CHANNELS)
        file.setsampwidth(instrument.input.audio.get_sample_size(instrument.input.audio.get_format_from_width(WIDTH)))
        file.setframerate(RATE)
        
        #Write and Close the File
        file.writeframes(b''.join(instrument.input.frames))
        file.close()