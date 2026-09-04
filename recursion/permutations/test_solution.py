from solution import permute


def test_standard_case():
    result = sorted(permute([1, 2, 3]))
    expected = sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
    assert result == expected


def test_single_element():
    assert permute([1]) == [[1]]


def test_two_elements():
    result = sorted(permute([1, 2]))
    assert result == [[1, 2], [2, 1]]
