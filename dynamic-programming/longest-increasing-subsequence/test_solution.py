from solution import length_of_lis


def test_standard_case():
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4  # e.g. [2,3,7,101]


def test_all_increasing():
    assert length_of_lis([1, 2, 3, 4]) == 4


def test_all_decreasing():
    assert length_of_lis([4, 3, 2, 1]) == 1


def test_empty_array():
    assert length_of_lis([]) == 0


def test_single_element():
    assert length_of_lis([5]) == 1
