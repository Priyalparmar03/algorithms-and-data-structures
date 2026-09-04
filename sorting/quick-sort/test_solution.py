from solution import quick_sort


def test_unsorted_array():
    assert quick_sort([5, 2, 4, 1, 3]) == [1, 2, 3, 4, 5]


def test_already_sorted_worst_case_input():
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_reverse_sorted():
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_empty_array():
    assert quick_sort([]) == []


def test_duplicates():
    assert quick_sort([3, 1, 3, 2]) == [1, 2, 3, 3]
