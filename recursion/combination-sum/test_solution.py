from solution import combination_sum


def test_standard_case():
    result = sorted(sorted(c) for c in combination_sum([2, 3, 6, 7], 7))
    expected = sorted(sorted(c) for c in [[2, 2, 3], [7]])
    assert result == expected


def test_no_combination_possible():
    assert combination_sum([2, 4], 7) == []


def test_target_equals_single_candidate():
    assert combination_sum([2, 3, 5], 5) == [[5]] or [2, 3] in combination_sum([2, 3, 5], 5)
