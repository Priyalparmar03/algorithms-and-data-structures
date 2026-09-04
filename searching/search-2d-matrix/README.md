# Search 2D Matrix

**Source:** LeetCode #74
**Topic:** Searching
**Difficulty:** Medium

## Problem
Given an m x n matrix where each row is sorted and the first element of each row is greater than the last element of the previous row, search for a target value.

## Approach
The whole matrix is really just a single sorted array in disguise — treat it as flat with length m*n, and convert a flat index back to (row, col) via divmod. Run standard binary search on the flat index space; no need to build an actual flattened copy.

## Complexity
- Time: O(log(m*n)) — single binary search over the flattened index space.
- Space: O(1).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
