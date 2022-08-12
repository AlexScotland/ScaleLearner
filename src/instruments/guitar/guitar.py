from src.instruments.interfaces import Instrument
from src.theory.factories import NoteFactory
from src.theory.helpers import *
from .settings import *

class Guitar(Instrument):
    
    def __init__(self, tuning: list = STRING_TUNE, fret: int = FRET_COUNT):
        self.tuning = tuning
        self.frets = fret
        self.strings = self.__generate_notes_from_tuning()

    def __generate_notes_from_tuning(self) -> dict:
        strings = {}
        piano = NoteFactory.create_piano_roll()
        for note in self.tuning:
            strings[note] = {}
            index_of_first_string = get_established_note_index_from_piano_roll(piano, note)
            for individual_fret in range(0, self.frets):
                strings[note][individual_fret] = {}
                strings[note][individual_fret] = piano[index_of_first_string + individual_fret]
        return strings
    
    def generate_guitar_neck(self):
        tab_string = "\n"
        for string in self.strings.keys():
            tab_string += f"{string.note}"
            for fret in self.strings[string].keys():
                if fret == 0:
                    # We dont tab 0's
                    continue
                tab_string += f" | {self.strings[string][fret].note}"
            tab_string +="\n"

        return tab_string

