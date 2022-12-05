from numpy import full
import pytest
from webserver.src.theory.helpers import *
from webserver.src.theory.models import Note
from webserver.src.theory.factories import NoteFactory

def test_correct_compare_notes():
    note1 = Note("A", 4, None)
    note2 = Note("A", 4, None)
    assert compare_notes(note1, note2)

def test_wrong_compare_notes():
    note1 = Note("A", 4, None)
    note2 = Note("A", 5, None)
    assert not compare_notes(note1, note2)

def test_get_established_note_from_unknown_step():
    full_note = get_note_from_established_piano_roll(NoteFactory.create_piano_roll(), Note("A", 4, None))
    assert full_note.half_steps_from_c_zero == 58

def test_get_half_steps_between_notes():
    note1 = Note("C", 0)
    note2 = Note("Db", 0)
    assert get_half_steps_between_notes(note2, note1) == -1

def test_generate_frequency():
    assert generate_frequency(Note("C", 0)) == 16.351597831287375
    assert generate_frequency(Note("A", 4)) == 440
    assert generate_frequency(Note("A", 5)) == 880.0000000000003
    assert generate_frequency(Note("Db", 1)) == 34.647828872108946