from solution import subarray_sum


def test_standard_case():
    assert subarray_sum([1, 1, 1], 2) == 2


def test_with_negative_numbers():
    assert subarray_sum([1, -1, 0], 0) == 3


def test_no_match():
    assert subarray_sum([1, 2, 3], 100) == 0


def test_single_element_matches():
    assert subarray_sum([5], 5) == 1
