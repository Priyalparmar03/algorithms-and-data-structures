from solution import my_pow


def test_positive_exponent():
    assert my_pow(2.0, 10) == 1024.0


def test_negative_exponent():
    assert round(my_pow(2.0, -2), 4) == 0.25


def test_zero_exponent():
    assert my_pow(5.0, 0) == 1.0


def test_exponent_one():
    assert my_pow(3.0, 1) == 3.0
