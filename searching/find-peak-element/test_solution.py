from solution import find_peak_element


def test_single_peak():
    result = find_peak_element([1, 2, 3, 1])
    assert result == 2


def test_increasing_array():
    result = find_peak_element([1, 2, 3, 4])
    assert result == 3


def test_decreasing_array():
    result = find_peak_element([4, 3, 2, 1])
    assert result == 0


def test_single_element():
    assert find_peak_element([1]) == 0
