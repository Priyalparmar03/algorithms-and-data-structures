from solution import coin_change


def test_standard_case():
    assert coin_change([1, 2, 5], 11) == 3  # 5 + 5 + 1


def test_impossible_amount():
    assert coin_change([2], 3) == -1


def test_zero_amount():
    assert coin_change([1], 0) == 0


def test_exact_single_coin():
    assert coin_change([1, 2, 5], 5) == 1
