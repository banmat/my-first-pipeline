from main import multiply_numbers


def test_multiply_numbers_multiplies_two_positive_numbers():
    assert multiply_numbers(5, 5) == 25


def test_multiply_numbers_handles_zero():
    assert multiply_numbers(7, 0) == 0


def test_multiply_numbers_handles_negative_numbers():
    assert multiply_numbers(-3, 4) == -12
