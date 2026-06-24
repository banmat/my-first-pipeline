from main import multiply_numbers, subtract_numbers


def test_multiply_numbers_multiplies_two_positive_numbers():
    assert multiply_numbers(5, 5) == 25


def test_multiply_numbers_handles_zero():
    assert multiply_numbers(7, 0) == 0


def test_multiply_numbers_handles_negative_numbers():
    assert multiply_numbers(-3, 4) == -12


def test_subtract_numbers_subtracts_second_number():
    assert subtract_numbers(10, 4) == 6


def test_subtract_numbers_handles_negative_result():
    assert subtract_numbers(3, 8) == -5
