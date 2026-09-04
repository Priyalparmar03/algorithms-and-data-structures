from solution import build_list, to_list, reorder_list


def test_even_length():
    head = build_list([1, 2, 3, 4])
    reorder_list(head)
    assert to_list(head) == [1, 4, 2, 3]


def test_odd_length():
    head = build_list([1, 2, 3, 4, 5])
    reorder_list(head)
    assert to_list(head) == [1, 5, 2, 4, 3]


def test_single_node():
    head = build_list([1])
    reorder_list(head)
    assert to_list(head) == [1]
