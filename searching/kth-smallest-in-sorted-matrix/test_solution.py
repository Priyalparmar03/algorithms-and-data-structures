from solution import kth_smallest


def test_standard_case():
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    assert kth_smallest(matrix, 8) == 13


def test_smallest_element():
    matrix = [[1, 2], [3, 4]]
    assert kth_smallest(matrix, 1) == 1


def test_largest_element():
    matrix = [[1, 2], [3, 4]]
    assert kth_smallest(matrix, 4) == 4


def test_single_element_matrix():
    assert kth_smallest([[5]], 1) == 5
