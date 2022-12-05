import pytest
from webserver.src.theory.models import Scale, Note, Key
from webserver.src.theory.factories import ScaleFactory, NoteFactory


def test_create_major_scale_without_scale_object():
    major_key = Key([2,2,1,2,2,2,1],[5,7])
    e = Note("E",2)
    major_octave = major_key.get_notes_in_key(e, NoteFactory)
    expected_notes = [Note("E",2), Note("Gb",2), Note("Ab",2), Note("A",2), Note("B",2), Note("Db",3), Note("Eb",3), Note("E",3)]
    for index in range(len(major_octave)):
        assert major_octave[index].note == expected_notes[index].note
        assert major_octave[index].octave == expected_notes[index].octave

def test_create_minor_scale_dynamically_without_scale_object():
    minor_key = Key([2,1,2,2,1,2,2],[3,5])
    e = Note("E",2)
    minor_octave = minor_key.get_notes_in_key(e, NoteFactory)
    expected_notes = [Note("E",2), Note("Gb",2), Note("G",2), Note("A",2), Note("B",2), Note("C",3), Note("D",3),  Note("E",3)]
    for index in range(len(minor_octave)):
        assert minor_octave[index].note == expected_notes[index].note
        assert minor_octave[index].octave == expected_notes[index].octave
    
def test_create_major_scale_dynamically_with_scale_object():
    e = Note("E",2)
    major_key = Key([2,2,1,2,2,2,1],[5,7])
    scale = ScaleFactory.create_scale_from_key(e, major_key)
    assert isinstance(scale, Scale)
    expected_notes = [Note("E",2), Note("Gb",2), Note("Ab",2), Note("A",2), Note("B",2), Note("Db",3), Note("Eb",3)]
    for index in range(len(scale.notes)):
        assert scale.notes[index].note == expected_notes[index].note
        assert scale.notes[index].octave == expected_notes[index].octave