"""Detect Cycle in a Directed Graph — DFS with three-color node states."""
from typing import Dict, List


def has_cycle(graph: Dict[int, List[int]]) -> bool:
    UNVISITED, VISITING, VISITED = 0, 1, 2
    state = {node: UNVISITED for node in graph}

    def dfs(node) -> bool:
        state[node] = VISITING
        for neighbor in graph.get(node, []):
            if state.get(neighbor, UNVISITED) == VISITING:
                return True
            if state.get(neighbor, UNVISITED) == UNVISITED and dfs(neighbor):
                return True
        state[node] = VISITED
        return False

    return any(state[node] == UNVISITED and dfs(node) for node in graph)
