from solution import find_kth_largest


def test_standard_case():
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5


def test_with_duplicates():
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


def test_k_equals_1_finds_max():
    assert find_kth_largest([1, 2, 3], 1) == 3


def test_k_equals_length_finds_min():
    assert find_kth_largest([1, 2, 3], 3) == 1
