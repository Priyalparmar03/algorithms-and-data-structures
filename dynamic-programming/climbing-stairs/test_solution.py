from solution import climb_stairs


def test_base_cases():
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2


def test_standard_case():
    assert climb_stairs(5) == 8


def test_larger_value():
    assert climb_stairs(10) == 89
