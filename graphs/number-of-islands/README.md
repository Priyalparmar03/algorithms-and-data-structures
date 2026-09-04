# Number Of Islands

**Source:** LeetCode #200
**Topic:** Graphs
**Difficulty:** Medium

## Problem
Given a 2D grid of '1's (land) and '0's (water), count the number of islands (connected groups of land, connected horizontally/vertically).

## Approach
Scan every cell; whenever an unvisited '1' is found, it's a new island — run DFS (or BFS) from it to mark every connected land cell as visited so it isn't counted again, then increment the island count. This is the canonical 'connected components on a grid' pattern.

## Complexity
- Time: O(rows x cols) — every cell visited a constant number of times.
- Space: O(rows x cols) worst case for the DFS recursion stack (all-land grid).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
Mutating the input grid in place to mark visited cells is memory-efficient but destroys the caller's data — in a real system I'd use a separate visited set instead, and would call that trade-off out explicitly.
