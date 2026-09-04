from solution import Node, clone_graph


def test_triangle_graph():
    n1, n2, n3 = Node(1), Node(2), Node(3)
    n1.neighbors = [n2, n3]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n1, n2]

    cloned = clone_graph(n1)
    assert cloned is not n1
    assert cloned.val == 1
    assert {n.val for n in cloned.neighbors} == {2, 3}
    # cloned graph must not reference original nodes
    assert all(n is not n1 and n is not n2 and n is not n3 for n in cloned.neighbors)


def test_single_node_no_neighbors():
    n1 = Node(1)
    cloned = clone_graph(n1)
    assert cloned.val == 1
    assert cloned.neighbors == []


def test_none_input():
    assert clone_graph(None) is None
