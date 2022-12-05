from abc import ABC, abstractmethod

class IKey(ABC):

    @abstractmethod
    def get_notes_in_key():
        pass

    @abstractmethod
    def create_chord_from_root_note():
        pass