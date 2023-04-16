import pytest
from model.blood_type import BloodType


def test_donors_for_blood_type_a_positive():
    a_positive = BloodType(antigen="A", protein="+")
    assert BloodType.get_compatible_donors(recipient_blood_type=a_positive)