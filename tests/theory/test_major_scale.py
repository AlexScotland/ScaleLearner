import pytest
from src.theory.models import Scale
from src.theory.models import Note
from src.theory.factories import ScaleFactory

def test_create_major_scale():
    e_major_scale = ScaleFactory.create_major_scale(Note("E",2))
    assert e_major_scale.root.note == "E"
    assert e_major_scale.steps == [2, 2, 1, 2, 2, 2, 1]
    excpected_notes = [Note("E",2), Note("Gb",2), Note("Ab",2), Note("A",2), Note("B",2), Note("Db",3), Note("Eb",3)]
    for index in range(len(e_major_scale.notes)):
        assert e_major_scale.notes[index].note == excpected_notes[index].note
        assert e_major_scale.notes[index].octave == excpected_notes[index].octave