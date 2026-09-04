# Clone Graph

**Source:** LeetCode #133
**Topic:** Graphs
**Difficulty:** Medium

## Problem
Given a reference to a node in a connected undirected graph, return a deep copy (clone) of the graph.

## Approach
DFS with a hash map from original node to its clone. Before recursing into a node's neighbors, create and register its clone in the map immediately — this handles cycles correctly, since when DFS reaches a node again via a different path, the map lookup returns the already-created clone instead of infinite-looping.

## Complexity
- Time: O(V + E) — every node and edge visited once.
- Space: O(V) — hash map plus recursion stack.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
