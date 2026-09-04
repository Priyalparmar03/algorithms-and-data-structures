# Find First And Last Position

**Source:** LeetCode #34
**Topic:** Searching
**Difficulty:** Medium

## Problem
Given a sorted array, find the starting and ending index of a given target value in O(log n).

## Approach
A single binary search finds *a* occurrence but not necessarily the first or last. Run two modified binary searches: one biased to keep searching left even after finding a match (to find the leftmost occurrence), and one biased to keep searching right (to find the rightmost). This is a common binary-search variant worth having as a reusable pattern.

## Complexity
- Time: O(log n) — two binary searches.
- Space: O(1).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
