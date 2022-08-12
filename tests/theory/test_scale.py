import pytest
from src.theory.models import Scale, Note, Key
from src.theory.factories import ScaleFactory

def test_create_major_scale():
    minor_key = Key([2,2,1,2,2,2,1],[5,7])
    e = Note("E",2)
    major_octave = minor_key.get_notes_in_key(e)
    expected_notes = [Note("E",2), Note("Gb",2), Note("Ab",2), Note("A",2), Note("B",2), Note("Db",3), Note("Eb",3), Note("E",3)]
    for index in range(len(major_octave)):
        assert major_octave[index].note == expected_notes[index].note
        assert major_octave[index].octave == expected_notes[index].octave

def test_create_minor_scale_dynamically():
    minor_key = Key([2,1,2,2,1,2,2],[3,5])
    e = Note("E",2)
    minor_octave = minor_key.get_notes_in_key(e)
    expected_notes = [Note("E",2), Note("Gb",2), Note("G",2), Note("A",2), Note("B",2), Note("C",3), Note("D",3),  Note("E",3)]
    for index in range(len(minor_octave)):
        assert minor_octave[index].note == expected_notes[index].note
        assert minor_octave[index].octave == expected_notes[index].octave