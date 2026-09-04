from solution import build_list, to_list, reverse_list


def test_standard_case():
    head = build_list([1, 2, 3, 4, 5])
    assert to_list(reverse_list(head)) == [5, 4, 3, 2, 1]


def test_empty_list():
    assert reverse_list(None) is None


def test_single_node():
    head = build_list([1])
    assert to_list(reverse_list(head)) == [1]
