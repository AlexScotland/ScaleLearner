from src.theory.models import Note
from src.theory.settings import ALL_NOTES

class NoteFactory():
    
    def create_piano_roll(height = 8):
        piano_roll = []
        half_steps_from_c_zero = 1
        octave = 0
        while octave < height + 1:
            for note in ALL_NOTES:
                piano_roll.append(Note(note, octave, half_steps_from_c_zero))
                half_steps_from_c_zero += 1
            octave += 1
        return piano_roll