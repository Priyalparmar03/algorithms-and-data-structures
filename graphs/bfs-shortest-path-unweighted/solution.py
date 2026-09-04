"""BFS shortest path (unweighted graph) — distance + parent reconstruction."""
from collections import deque
from typing import Dict, List, Optional


def bfs_shortest_paths(graph: Dict[int, List[int]], source: int):
    distance = {source: 0}
    parent = {source: None}
    queue = deque([source])
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, []):
            if neighbor not in distance:
                distance[neighbor] = distance[node] + 1
                parent[neighbor] = node
                queue.append(neighbor)
    return distance, parent


def reconstruct_path(parent: Dict[int, Optional[int]], target: int) -> List[int]:
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = parent.get(node)
    return path[::-1]
