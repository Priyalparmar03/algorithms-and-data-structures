from solution import build_list, to_list, add_two_numbers


def test_standard_case():
    # 342 + 465 = 807, represented reversed
    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])
    assert to_list(add_two_numbers(l1, l2)) == [7, 0, 8]


def test_carry_overflow():
    l1 = build_list([9, 9])
    l2 = build_list([1])
    assert to_list(add_two_numbers(l1, l2)) == [0, 0, 1]


def test_different_lengths():
    l1 = build_list([9])
    l2 = build_list([1, 9, 9])
    assert to_list(add_two_numbers(l1, l2)) == [0, 0, 0, 1]
