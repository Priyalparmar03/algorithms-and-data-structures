# Bfs Shortest Path Unweighted

**Source:** Classic / GeeksforGeeks
**Topic:** Graphs
**Difficulty:** Medium

## Problem
Given an unweighted graph and a source node, find the shortest path (in number of edges) from source to every other reachable node.

## Approach
BFS naturally explores nodes in order of increasing distance from the source, since it processes all nodes at distance k before any node at distance k+1. Track distance and a parent pointer for each node as it's first discovered (first discovery = shortest path, since BFS never revisits), then optionally reconstruct the actual path by walking parent pointers backward from any target.

## Complexity
- Time: O(V + E) — each node and edge processed once.
- Space: O(V) — distance array, parent array, and queue.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
