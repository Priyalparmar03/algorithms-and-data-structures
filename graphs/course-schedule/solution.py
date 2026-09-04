"""Course Schedule — cycle detection in a directed graph via DFS coloring."""
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph = {i: [] for i in range(num_courses)}
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    UNVISITED, VISITING, VISITED = 0, 1, 2
    state = [UNVISITED] * num_courses

    def has_cycle(node) -> bool:
        if state[node] == VISITING:
            return True
        if state[node] == VISITED:
            return False
        state[node] = VISITING
        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True
        state[node] = VISITED
        return False

    return not any(has_cycle(c) for c in range(num_courses))
