import pytest
from your_module import calculate_check_digit, update_barcode

def test_calculate_check_digit():
    assert calculate_check_digit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
    assert calculate_check_digit([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0

def test_update_barcode():
    barcode = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    updated_barcode = update_barcode(barcode)
    assert updated_barcode[-1] == calculate_check_digit(barcode[:-1])

def test_update_barcode_empty_list():
    with pytest.raises(ValueError):
        update_barcode([])

def test_update_barcode_invalid_input():
    with pytest.raises(TypeError):
        update_barcode("invalid input")
