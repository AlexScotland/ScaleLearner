from src.theory.models import Note

class Chord():
    
    def __init__(self, root: Note, second_note: Note, third_note: Note):
        self.root_note = root
        self.second_note = second_note
        self.third_note = third_note
    
    def __str__(self) -> list:
        return [
                self.root_note,
                self.second_note,
                self.third_note,
            ]