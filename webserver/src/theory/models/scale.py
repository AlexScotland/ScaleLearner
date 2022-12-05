from . import Note
from webserver.src.theory.helpers import get_next_note_in_scale, get_note_from_established_piano_roll

class Scale():
    def __init__(self, root_note: Note, steps: list, notes: list):
        self.root = root_note
        self.steps = steps
        self.notes = self.get_notes_from_steps(notes)

    def get_notes_from_steps(self, notes: list):
        self.root = get_note_from_established_piano_roll(notes, self.root)
        list_of_notes = []
        current_note = self.root
        for step in self.steps:
            list_of_notes.append(current_note)
            current_note = get_next_note_in_scale(current_note, notes, step)
        return list_of_notes