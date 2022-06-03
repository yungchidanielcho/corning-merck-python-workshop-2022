""" Test the functions in func.py """
import pytest
from so2_emission.preprocessing.func import row_is_valid, row_to_list
from datetime import datetime


def test_row_is_valid():
    row = "42430.29167\t2430\t857.32\n"
    assert row_is_valid(row) is True

def test_row_is_valid_false_case():
    row_is_false = "42430.29167\t2406.4\t-999\n"
    assert row_is_valid(row_is_false) is False

def test_row_to_list():
    row = "42430.29167\t2430\t857.32\n"
    row_to_list_result = row_to_list(row)

    assert isinstance(row_to_list_result, list)
    assert isinstance(row_to_list_result[0], datetime)
    expected_dt = datetime(year=2016, month=3, day=1, hour=0)
    assert row_to_list_result[0] == expected_dt
    assert isinstance(row_to_list_result[1], (int, float))
    assert pytest.approx()

