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
    
    def get_all_note_positions(self, note: Note) -> str:
        return self.find_all_note_on_neck(note)


    def find_all_note_on_neck(self, note: Note) -> dict:
        strings = self.strings
        note_to_find = note.note
        for string in strings.keys():
            for fret in strings[string].keys():
                if strings[string][fret].note == note_to_find:
                    strings[string][fret].note = fret
        return self.__generate_tab_from_string(strings)
    
    def __generate_tab_from_string(self, strings: dict) -> str:
        tab_string = "\n"
        for string in strings.keys():
            tab_string += f"{string.note}"
            for fret in strings[string].keys():
                if isinstance(strings[string][fret].note, int):
                    tab_string += f" | {fret}"
                else:
                    tab_string += f" |  "
            tab_string +="\n"

        return tab_string
    
    def generate_guitar_neck(self, strings):
        tab_string = "\n"
        for string in strings.keys():
            tab_string += f"{string.note}"
            for fret in strings[string].keys():
                if fret == 0:
                    # We dont tab 0's
                    continue
                tab_string += f" | {strings[string][fret].note}"
            tab_string +="\n"

        return tab_string

