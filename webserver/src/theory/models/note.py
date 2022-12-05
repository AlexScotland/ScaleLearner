from webserver.src.theory import ALL_NOTES

class Note():

    def __init__(self, note, octave, half_steps_from_c_zero = None):
        self.note = note
        self.octave = octave
        self.half_steps_from_c_zero = half_steps_from_c_zero
