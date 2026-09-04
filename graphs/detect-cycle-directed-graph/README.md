# Detect Cycle Directed Graph

**Source:** Classic
**Topic:** Graphs
**Difficulty:** Medium

## Problem
Given a directed graph, detect whether it contains a cycle.

## Approach
Same three-state DFS coloring as course-schedule (unvisited / visiting / visited) — this is presented as its own standalone problem here because cycle detection is a fundamental building block reused across many graph problems (course scheduling, deadlock detection, dependency resolution), so it's worth having in isolation as reusable evidence.

## Complexity
- Time: O(V + E) — each node and edge visited once.
- Space: O(V) — state array plus recursion stack.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
