from solution import two_sum


def test_standard_case():
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]


def test_negative_numbers():
    assert sorted(two_sum([-3, 4, 3, 90], 0)) == [0, 2]


def test_duplicate_values():
    assert sorted(two_sum([3, 3], 6)) == [0, 1]


def test_target_at_end():
    assert sorted(two_sum([1, 2, 3, 4, 5], 9)) == [3, 4]
