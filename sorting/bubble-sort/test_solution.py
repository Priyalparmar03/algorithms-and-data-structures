from solution import bubble_sort


def test_unsorted_array():
    assert bubble_sort([5, 2, 4, 1, 3]) == [1, 2, 3, 4, 5]


def test_already_sorted():
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]


def test_reverse_sorted():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_empty_array():
    assert bubble_sort([]) == []


def test_duplicates():
    assert bubble_sort([3, 1, 3, 2]) == [1, 2, 3, 3]
