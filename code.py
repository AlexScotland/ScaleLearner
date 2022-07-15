from src.instruments.guitar.controller import Guitar
from src.inputs import MicrophoneJack
from src.outputs.file_exporter import ExportAudio

def record_audio():
    exporter = ExportAudio()
    main_guitar = Guitar(MicrophoneJack())
    main_guitar.input.open_live_audio_stream()
    main_guitar.input.capture_audio_data(export=True)
    exporter.export_audio(main_guitar, "testing.wav")