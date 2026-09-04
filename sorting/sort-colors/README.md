# Sort Colors

**Source:** LeetCode #75
**Topic:** Sorting
**Difficulty:** Medium

## Problem
Given an array with only values 0, 1, and 2, sort it in place in one pass (Dutch National Flag problem).

## Approach
Standard sorting would be O(n log n) or need counting in two passes. The Dutch flag algorithm uses three pointers: `low` (boundary for 0s), `mid` (current element), and `high` (boundary for 2s). Swap 0s to the front, leave 1s in place (advance mid), and swap 2s to the back — but when swapping with high, don't advance mid, since the swapped-in value from the back hasn't been examined yet.

## Complexity
- Time: O(n) — single pass, each element examined a constant number of times.
- Space: O(1) — in place, three pointers.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
