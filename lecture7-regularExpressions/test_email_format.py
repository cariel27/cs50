import pytest
from validate_email import is_email_valid


def test_valid_email():
    assert is_email_valid(email="cibanez@harvard.edu") is True


def test_valid_email_username_uppercase():
    assert is_email_valid(email="CIBANEZ@harvard.edu") is True


def test_valid_email_domain_uppercase():
    assert is_email_valid(email="cibanez@HARVARD.EDU") is True


def test_valid_email_uppercase():
    assert is_email_valid(email="CIBANEZ@HARVARD.EDU") is True


def test_valid_email_username_with_dots():
    assert is_email_valid(email="cristian.ariel.ibanez@harvard.edu") is True


def test_valid_email_domain_with_one_dot():
    assert is_email_valid(email="cristianarielibanez@harvard.edu") is True


def test_valid_email_domain_with_two_dots():
    assert is_email_valid(email="cristianarielibanez@cs50.harvard.edu") is True


def test_valid_email_domain_with_three_dots():
    assert is_email_valid(email="cristianarielibanez@cs50.ed.harvard.edu") is True


def test_valid_email_username_with_period():
    assert is_email_valid(email="cristian-ariel-ibanez@harvard.edu") is True


def test_valid_email_domain_with_period():
    assert is_email_valid(email="cristianarielibanez@it-harvard.edu") is True


def test_valid_email_username_with_underscore():
    assert is_email_valid(email="cristian_ariel_ibanez@harvard.edu") is True


def test_valid_email_domain_with_underscore():
    assert is_email_valid(email="cristianarielibanez@it_harvard.edu") is True


def test_username_with_space():
    assert is_email_valid(email="cib anez@harvard.edu") is False


def test_domain_with_space():
    assert is_email_valid(email="cibanez@har vard.edu") is False


def test_username_and_domain_with_space():
    assert is_email_valid(email="cib anez@har vard.edu") is False


def test_username_with_at():
    assert is_email_valid(email="cib@@anez@harvard.edu") is False


def test_domain_with_at():
    assert is_email_valid(email="cibanez@harva@@rd.edu") is False


def test_domain_with_trailing_dot():
    assert is_email_valid(email="cibanez@harvard.edu.") is False


def test_username_with_special_chars():
    assert is_email_valid(email="cib!$%anez@harvard.edu$") is False


def test_domain_with_special_chars():
    assert is_email_valid(email="cibanez@har!$%vard.edu$") is False
