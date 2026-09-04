# Graph Valid Tree

**Source:** LeetCode #261 (Premium)
**Topic:** Graphs
**Difficulty:** Medium

## Problem
Given n nodes labeled 0 to n-1 and a list of undirected edges, determine whether these edges form a valid tree.

## Approach
A valid tree on n nodes has exactly two properties: (1) exactly n-1 edges, and (2) it's fully connected (no disconnected components). Check the edge count first as a cheap early exit, then run BFS/DFS from node 0 and verify every node was reached — that confirms connectivity. (A graph with n-1 edges and no cycles is automatically connected iff it reaches all n nodes, so this check alone is sufficient, no separate cycle check needed.)

## Complexity
- Time: O(V + E) — one BFS/DFS pass.
- Space: O(V + E) — adjacency list plus visited set.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
