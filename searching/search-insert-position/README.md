# Search Insert Position

**Source:** LeetCode #35
**Topic:** Searching
**Difficulty:** Easy

## Problem
Given a sorted array and a target, return the index if found, or the index where it would be inserted to keep the array sorted.

## Approach
This is standard binary search with one small change: instead of returning -1 on failure, return `low` at the end of the loop — by the time the loop exits, `low` has naturally converged to exactly the correct insertion point, whether or not the target was actually found.

## Complexity
- Time: O(log n).
- Space: O(1).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
