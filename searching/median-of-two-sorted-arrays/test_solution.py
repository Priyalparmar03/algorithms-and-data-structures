from solution import find_median_sorted_arrays


def test_odd_total_length():
    assert find_median_sorted_arrays([1, 3], [2]) == 2.0


def test_even_total_length():
    assert find_median_sorted_arrays([1, 2], [3, 4]) == 2.5


def test_one_array_empty():
    assert find_median_sorted_arrays([], [1]) == 1.0


def test_no_overlap():
    assert find_median_sorted_arrays([1, 2], [-1, 3]) == 1.5
