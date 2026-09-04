from solution import build_list, to_list, merge_two_lists


def test_standard_case():
    l1 = build_list([1, 2, 4])
    l2 = build_list([1, 3, 4])
    assert to_list(merge_two_lists(l1, l2)) == [1, 1, 2, 3, 4, 4]


def test_one_empty():
    l1 = build_list([])
    l2 = build_list([0])
    assert to_list(merge_two_lists(l1, l2)) == [0]


def test_both_empty():
    assert to_list(merge_two_lists(build_list([]), build_list([]))) == []
