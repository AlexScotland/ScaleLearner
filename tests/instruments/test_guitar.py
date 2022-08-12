from src.instruments.guitar import Guitar, settings
from src.theory.models import Note
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

def generate_guitar_neck():
    guitar = Guitar()
    assert isinstance(guitar.generate_guitar_neck(), str)