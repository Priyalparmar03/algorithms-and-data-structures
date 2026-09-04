from solution import three_sum


def test_standard_case():
    result = sorted(sorted(t) for t in three_sum([-1, 0, 1, 2, -1, -4]))
    expected = sorted(sorted(t) for t in [[-1, -1, 2], [-1, 0, 1]])
    assert result == expected


def test_no_triplet():
    assert three_sum([0, 1, 1]) == []


def test_all_zeros():
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
