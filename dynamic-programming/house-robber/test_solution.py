from solution import rob


def test_standard_case():
    assert rob([1, 2, 3, 1]) == 4  # rob house 0 and house 2: 1 + 3


def test_alternating_better():
    assert rob([2, 7, 9, 3, 1]) == 12  # rob houses 0, 2, 4: 2 + 9 + 1


def test_empty_array():
    assert rob([]) == 0


def test_single_house():
    assert rob([5]) == 5


def test_two_houses():
    assert rob([2, 1]) == 2
