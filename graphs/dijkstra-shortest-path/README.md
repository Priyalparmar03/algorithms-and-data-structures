# Dijkstra Shortest Path

**Source:** Classic
**Topic:** Graphs
**Difficulty:** Medium

## Problem
Given a weighted graph with non-negative edge weights and a source node, find the shortest path distance from source to all other nodes.

## Approach
BFS finds shortest paths by edge *count*, which breaks once edges have different weights. Dijkstra's fixes this with a min-heap priority queue: always expand the unvisited node with the smallest known distance so far, and relax (potentially improve) its neighbors' distances. Skip stale heap entries (a node popped with a distance worse than its current best) rather than removing them from the heap, which is simpler than a full decrease-key operation.

## Complexity
- Time: O((V + E) log V) — each edge relaxation is an O(log V) heap push/pop.
- Space: O(V + E) — adjacency list, distance dict, heap.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
