from webserver.src.instruments.guitar import Guitar
from webserver.src.theory.helpers import *
import copy

class APIGuitar(Guitar):
    
    def get_all_note_positions_for_api(self, note: Note) -> dict:
        return self.__generate_json_tab_from_string(self.find_all_note_on_neck(note))
    
    def __generate_json_tab_from_string(self, strings: dict) -> str:
        string_dict = self.__generate_api_string_dict()
        for string in strings.keys():
            for fret in strings[string].keys():
                if hasattr(strings[string][fret], "fretted"):
                    string_dict[string.note].append(fret)
        return string_dict
    
    def __generate_api_string_dict(self) -> dict:
        temp_dict = {}
        for key in self.strings:
            temp_dict[key.note] = []
        return temp_dict