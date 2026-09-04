# Course Schedule

**Source:** LeetCode #207
**Topic:** Graphs
**Difficulty:** Medium

## Problem
Given `numCourses` and a list of prerequisite pairs [a, b] (must take b before a), determine if it's possible to finish all courses (i.e., the prerequisite graph has no cycle).

## Approach
This is cycle detection in a directed graph. Do DFS while tracking each node's state: unvisited, currently-in-the-recursion-stack ('visiting'), or fully processed ('visited'). If DFS reaches a node that's currently 'visiting', that's a back edge — a cycle — so it's impossible. Alternative: Kahn's algorithm (topological sort via in-degree/BFS) also solves this and additionally gives a valid course order.

## Complexity
- Time: O(V + E) — each node and edge visited once.
- Space: O(V) — adjacency list, state array, recursion stack.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
