from solution import longest_consecutive


def test_standard_case():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4


def test_empty_array():
    assert longest_consecutive([]) == 0


def test_with_duplicates():
    assert longest_consecutive([1, 2, 2, 3]) == 3


def test_no_consecutive():
    assert longest_consecutive([10, 5, 100]) == 1
