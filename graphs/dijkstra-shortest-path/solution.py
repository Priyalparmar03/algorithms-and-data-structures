"""Dijkstra's Algorithm — min-heap priority queue, non-negative weights only."""
import heapq
from typing import Dict, List, Tuple


def dijkstra(graph: Dict[int, List[Tuple[int, int]]], source: int) -> Dict[int, float]:
    """graph[node] = list of (neighbor, weight) tuples."""
    distance = {source: 0}
    heap = [(0, source)]
    visited = set()

    while heap:
        dist, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph.get(node, []):
            new_dist = dist + weight
            if new_dist < distance.get(neighbor, float("inf")):
                distance[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distance
