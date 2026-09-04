from solution import subsets


def test_standard_case():
    result = sorted(sorted(s) for s in subsets([1, 2, 3]))
    expected = sorted(sorted(s) for s in
                       [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
    assert result == expected


def test_empty_input():
    assert subsets([]) == [[]]


def test_single_element():
    result = sorted(sorted(s) for s in subsets([1]))
    assert result == [[], [1]]
