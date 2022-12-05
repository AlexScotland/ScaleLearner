from webserver.src.theory.models import Scale, Note
from webserver.src.theory.factories import NoteFactory
from webserver.src.theory.interfaces import IKey

class ScaleFactory():

    def create_major_scale(root_note: Note) -> Scale:
        return Scale(root_note, [2, 2, 1, 2, 2 ,2, 1], NoteFactory.create_piano_roll()) 
    
    def create_scale_from_key(root_note: Note, key: IKey) -> Scale:
        return Scale(root_note, key.octave_steps, NoteFactory.create_piano_roll()) 