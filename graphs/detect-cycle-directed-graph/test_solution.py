from solution import has_cycle


def test_with_cycle():
    graph = {0: [1], 1: [2], 2: [0]}
    assert has_cycle(graph) is True


def test_no_cycle_dag():
    graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
    assert has_cycle(graph) is False


def test_disconnected_components_one_with_cycle():
    graph = {0: [1], 1: [], 2: [3], 3: [2]}
    assert has_cycle(graph) is True


def test_empty_graph():
    assert has_cycle({}) is False
