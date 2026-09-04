from solution import binary_search


def test_found_middle():
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4


def test_not_found():
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1


def test_empty_array():
    assert binary_search([], 5) == -1


def test_single_element_found():
    assert binary_search([5], 5) == 0
