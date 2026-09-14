from solution import product_except_self


def test_standard_case():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]

def test_with_zero():
    assert product_except_self([1, 2, 0, 4]) == [0, 0, 8, 0]

def test_two_zeros():
    assert product_except_self([0, 4, 0]) == [0, 0, 0]

def test_negative_numbers():
    assert product_except_self([-1, 2, -3]) == [-6, 3, -2]
