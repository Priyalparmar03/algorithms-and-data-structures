from solution import search


def test_target_in_rotated_part():
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_target_in_sorted_part():
    assert search([4, 5, 6, 7, 0, 1, 2], 5) == 1


def test_not_found():
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_no_rotation():
    assert search([1, 2, 3, 4, 5], 3) == 2


def test_single_element():
    assert search([1], 1) == 0
