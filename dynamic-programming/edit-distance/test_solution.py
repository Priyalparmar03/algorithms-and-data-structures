from solution import min_distance


def test_standard_case():
    assert min_distance("horse", "ros") == 3


def test_identical_strings():
    assert min_distance("abc", "abc") == 0


def test_one_empty_string():
    assert min_distance("", "abc") == 3


def test_both_empty():
    assert min_distance("", "") == 0


def test_completely_different():
    assert min_distance("intention", "execution") == 5
