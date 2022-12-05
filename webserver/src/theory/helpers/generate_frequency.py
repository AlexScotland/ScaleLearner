from webserver.src.theory.models import Note
from webserver.src.theory.settings import ALL_NOTES
from math import pow

def generate_frequency(note : Note) -> int:
    """
    Using the A4 note (440hz), 
    this function will calculate the hz by the count of steps between A4 and desired note object.
    """
    a_four = Note("A", 4)
    half_step_frequency = pow(2,1/12)
    steps = get_half_steps_between_notes(a_four, note)
    return 440 * pow(half_step_frequency, steps)

def get_note_from_established_piano_roll(piano_roll: list, note: Note) -> Note:
    for potential_note in piano_roll:
        if compare_notes(potential_note, note):
            return potential_note
    return None

def compare_notes(note1: Note, note2: Note) -> bool:
    returner = True if note1.note == note2.note and note1.octave == note2.octave else False
    return returner

def get_half_steps_between_notes(note1: Note, note2: Note) -> int:
    note1.half_steps_from_c_zero = (12 * note1.octave) + get_note_from_piano_roll(note1)
    note2.half_steps_from_c_zero = (12 * note2.octave) + get_note_from_piano_roll(note2)
    return note2.half_steps_from_c_zero - note1.half_steps_from_c_zero


def get_note_from_piano_roll(note: Note) -> int:
    for index in range(len(ALL_NOTES)):
        if ALL_NOTES[index] == note.note:
            return index
    return None

def get_established_note_index_from_piano_roll(piano_roll: list, note: Note) -> int:
    for index in range(len(piano_roll)):
        if compare_notes(piano_roll[index], note):
            return index
    return None

def get_next_note_in_scale(note: Note, note_list: list, step: int) -> Note:
    return note_list[note_list.index(note) + step]