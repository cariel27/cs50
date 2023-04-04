import pytest
from name_format import get_format_name

EXPECTED = "Ariel Ibañez"


def test_validate_name_with_comma():
    assert get_format_name(input_str="Ibañez, Ariel") == EXPECTED


def test_validate_name_with_no_comma():
    assert get_format_name(input_str="Ariel Ibañez") == EXPECTED


def test_validate_name_with_comma_without_space():
    assert get_format_name(input_str="Ibañez,Ariel") == EXPECTED


def test_validate_name_with_comma_with_spaces():
    assert get_format_name(input_str="Ibañez,       Ariel") == EXPECTED
