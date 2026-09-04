from solution import tower_of_hanoi


def test_move_count_is_2_pow_n_minus_1():
    assert len(tower_of_hanoi(3)) == 7  # 2^3 - 1
    assert len(tower_of_hanoi(4)) == 15  # 2^4 - 1


def test_single_disk():
    assert tower_of_hanoi(1) == [("A", "C")]


def test_zero_disks():
    assert tower_of_hanoi(0) == []


def test_two_disks_sequence():
    assert tower_of_hanoi(2) == [("A", "B"), ("A", "C"), ("B", "C")]
