from solution import counting_sort


def test_unsorted_array():
    assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]


def test_already_sorted():
    assert counting_sort([1, 2, 3]) == [1, 2, 3]


def test_all_same_value():
    assert counting_sort([5, 5, 5]) == [5, 5, 5]


def test_empty_array():
    assert counting_sort([]) == []
