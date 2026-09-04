from solution import build_list, to_list, remove_nth_from_end


def test_standard_case():
    head = build_list([1, 2, 3, 4, 5])
    assert to_list(remove_nth_from_end(head, 2)) == [1, 2, 3, 5]


def test_remove_head_single_node():
    head = build_list([1])
    assert to_list(remove_nth_from_end(head, 1)) == []


def test_remove_head_multiple_nodes():
    head = build_list([1, 2])
    assert to_list(remove_nth_from_end(head, 2)) == [2]
