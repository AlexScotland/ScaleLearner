import pytest
from src.theory.scales.models import Scale
from src.theory.scales.scale_objects import MinorScale

def test_minor_scale_starting_at_C():
    minor_scale = Scale(MinorScale())
    assert minor_scale.get_minor_scale("C") == ["C", "D", "Eb", "F", "G", "Ab", "Bb", "C"]

def test_minor_scale_starting_at_A():
    minor_scale = Scale(MinorScale())
    assert minor_scale.get_minor_scale("A") == ["A","B","C","D","E","F","G","A"]