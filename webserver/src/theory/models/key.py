from webserver.src.theory.interfaces import IKey
from webserver.src.theory.models import Note, Chord
from webserver.src.theory.helpers import *

class Key(IKey):

    def __init__(self, octave_steps: list, chord_steps: list):
        self.octave_steps = octave_steps
        self.chord_steps = chord_steps
        self.notes = None

    def get_notes_in_key(self, root_note: Note, note_factory):
        notes = []
        piano = note_factory.create_piano_roll()
        root_note_index = get_established_note_index_from_piano_roll(piano, get_note_from_established_piano_roll(piano, root_note))
        notes.append(piano[root_note_index])
        last_note = root_note_index
        for step in self.octave_steps:
            notes.append(piano[last_note + step])
            last_note += step
        return notes

    def create_chord_from_root_note(self, root_note: Note, note_factory):
        piano = note_factory.create_piano_roll()
        root_note_index = get_note_from_piano_roll(get_note_from_established_piano_roll(piano, root_note))
        return Chord(piano[root_note_index], piano[root_note_index + self.chord_steps[0]], piano[root_note_index + self.chord_steps[1]])