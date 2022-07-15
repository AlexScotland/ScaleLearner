from instruments import PIANO_ROLL

class Scale:
    def __init__(self, scale_object):
        self.scale = scale_object
        self.steps = self.scale.steps
    
    def get_minor_scale(self, root_note):
        note_index = PIANO_ROLL.index(root_note)
        returned_scale = [root_note]
        for step in self.steps:
            note_index += step
            if note_index >= len(PIANO_ROLL): note_index -= len(PIANO_ROLL)
            returned_scale.append(PIANO_ROLL[note_index])
        return returned_scale
