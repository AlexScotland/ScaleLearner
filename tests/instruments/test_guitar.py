from src.instruments.guitar import Guitar, settings
from src.theory.models import Note, Chord
import pytest

def test_creating_guitar():
    guitar = Guitar()
    assert guitar.strings[settings.STRING_TUNE[0]][0].note == settings.STRING_TUNE[0].note
    assert guitar.strings[settings.STRING_TUNE[0]][0].octave == settings.STRING_TUNE[0].octave
    # test 5th fret for proper tuning
    assert guitar.strings[settings.STRING_TUNE[0]][5].note == settings.STRING_TUNE[1].note
    assert guitar.strings[settings.STRING_TUNE[0]][5].octave == settings.STRING_TUNE[1].octave

def test_creating_guitar_with_drop_tuning():
    tuning = [Note("D", 2), Note("A", 2), Note("D", 3), Note("G", 3), Note("B", 3), Note("E", 4)]
    guitar = Guitar(tuning, 15)
    assert guitar.strings[tuning[0]][2].note == settings.STRING_TUNE[0].note
    assert guitar.strings[tuning[0]][2].octave == settings.STRING_TUNE[0].octave
    # test 5th fret for proper tuning
    assert guitar.strings[tuning[0]][7].note == settings.STRING_TUNE[1].note
    assert guitar.strings[tuning[0]][7].octave == settings.STRING_TUNE[1].octave

def test_get_all_e_notes_with_standard_tuning():
    guitar = Guitar()
    e = Note("E", 2)
    guitar_neck_with_e = guitar.get_all_note_positions(e)
    print("")
    print("All E Positions in Standard Tuning")
    print(guitar_neck_with_e)

def test_get_all_e_notes_with_drop_tuning():
    tuning = [Note("D", 2), Note("A", 2), Note("D", 3), Note("G", 3), Note("B", 3), Note("E", 4)]
    guitar = Guitar(tuning, 15)
    e = Note("E", 2)
    guitar_neck_with_e = guitar.get_all_note_positions(e)
    print("All E Positions in Drop D")
    print(guitar_neck_with_e)

def test_get_all_e_chords_with_standard_tuning():
    guitar = Guitar()
    e_chord = Chord(Note("E", 2), Note("B", 2), Note("E", 3))
    e_chords = guitar.get_all_notes_in_chord_positions(e_chord)
    print("All E Chords (E, B, E)")
    print(e_chords)

def generate_guitar_neck():
    guitar = Guitar()
    assert isinstance(guitar.generate_guitar_neck(guitar.strings), str)