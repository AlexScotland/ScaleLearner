import pytest
from webserver.src.theory.factories import NoteFactory
from webserver.src.theory.models import Note

def test_creation_of_piano_roll():
    piano_roll = NoteFactory.create_piano_roll()
    first_note = piano_roll[0]
    assert isinstance(first_note, Note)
    assert first_note.octave == 0
    assert first_note.note == "C"
    assert first_note.half_steps_from_c_zero == 1
    last_note = piano_roll[len(piano_roll)-1]
    assert isinstance(last_note, Note)
    assert last_note.octave == 8
    assert last_note.note == "B"
    assert last_note.half_steps_from_c_zero == 108