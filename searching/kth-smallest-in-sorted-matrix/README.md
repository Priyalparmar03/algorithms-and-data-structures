# Kth Smallest In Sorted Matrix

**Source:** LeetCode #378
**Topic:** Searching
**Difficulty:** Medium

## Problem
Given an n x n matrix where each row and column is sorted ascending, find the kth smallest element.

## Approach
Binary search on the *value range* (from matrix[0][0] to matrix[n-1][n-1]) rather than on indices: for a candidate value, count how many matrix elements are <= it in O(n) by walking from the bottom-left corner (moving up when a value is too big, right when counting a valid one) — the sorted rows/columns make this count linear instead of needing a full scan. Binary search that count against k to converge on the answer.

## Complexity
- Time: O(n log(max - min)) — n work per count, log(range) iterations of binary search on the value.
- Space: O(1) extra.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
A max-heap of size k (or min-heap merging rows) also solves this in O(n + k log n) and is more intuitive to explain, but the binary-search-on-value approach is the one to reach for when the interviewer specifically wants better-than-heap complexity.
