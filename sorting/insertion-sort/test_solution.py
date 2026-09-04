from solution import insertion_sort


def test_unsorted_array():
    assert insertion_sort([5, 2, 4, 1, 3]) == [1, 2, 3, 4, 5]


def test_already_sorted():
    assert insertion_sort([1, 2, 3]) == [1, 2, 3]


def test_reverse_sorted():
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_empty_array():
    assert insertion_sort([]) == []


def test_duplicates():
    assert insertion_sort([3, 1, 3, 2]) == [1, 2, 3, 3]
