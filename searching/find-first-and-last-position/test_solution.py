from solution import search_range


def test_standard_case():
    assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]


def test_not_found():
    assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]


def test_empty_array():
    assert search_range([], 0) == [-1, -1]


def test_single_occurrence():
    assert search_range([1, 2, 3], 2) == [1, 1]
