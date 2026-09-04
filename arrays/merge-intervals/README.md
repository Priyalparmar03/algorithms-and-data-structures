# Merge Intervals

**Source:** LeetCode #56
**Topic:** Arrays
**Difficulty:** Medium

## Problem
Given a list of intervals, merge all overlapping intervals and return the resulting non-overlapping set.

## Approach
Sort intervals by start time first — once sorted, overlaps can only happen between adjacent intervals in the sorted order. Walk through and merge into the last interval in the result whenever the current one's start is <= the last one's end; otherwise append it as a new interval.

## Complexity
- Time: O(n log n) — dominated by the sort.
- Space: O(n) — output list (or O(log n)/O(n) sort space depending on implementation).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
