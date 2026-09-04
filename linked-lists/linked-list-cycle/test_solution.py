from solution import ListNode, has_cycle


def test_no_cycle():
    a = ListNode(1)
    a.next = ListNode(2)
    assert has_cycle(a) is False


def test_empty_list():
    assert has_cycle(None) is False


def test_with_cycle():
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    a.next = b
    b.next = c
    c.next = b  # cycle back to b
    assert has_cycle(a) is True
