from solution import dijkstra


def test_standard_case():
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [],
    }
    result = dijkstra(graph, 0)
    assert result == {0: 0, 1: 3, 2: 1, 3: 4}


def test_unreachable_node_excluded():
    graph = {0: [(1, 1)], 1: [], 2: []}
    result = dijkstra(graph, 0)
    assert 2 not in result


def test_single_node():
    assert dijkstra({0: []}, 0) == {0: 0}
