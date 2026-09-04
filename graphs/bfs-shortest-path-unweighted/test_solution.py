from solution import bfs_shortest_paths, reconstruct_path


def build_graph():
    return {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2, 4], 4: [3]}


def test_distances():
    distance, _ = bfs_shortest_paths(build_graph(), 0)
    assert distance == {0: 0, 1: 1, 2: 1, 3: 2, 4: 3}


def test_path_reconstruction():
    _, parent = bfs_shortest_paths(build_graph(), 0)
    assert reconstruct_path(parent, 4) == [0, 1, 3, 4] or reconstruct_path(parent, 4) == [0, 2, 3, 4]


def test_unreachable_node():
    graph = {0: [1], 1: [0], 2: []}
    distance, _ = bfs_shortest_paths(graph, 0)
    assert 2 not in distance
