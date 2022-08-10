from src.theory.models import Scale, Note
from src.theory.factories import NoteFactory

class ScaleFactory():

    def create_major_scale(root_note: Note) -> Scale:
        return Scale(root_note, [2, 2, 1, 2, 2 ,2, 1], NoteFactory.create_piano_roll()) 