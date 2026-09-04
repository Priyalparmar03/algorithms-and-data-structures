# Search In Rotated Sorted Array

**Source:** LeetCode #33
**Topic:** Searching
**Difficulty:** Medium

## Problem
Given a rotated sorted array (e.g. [4,5,6,7,0,1,2]) with no duplicates, search for a target in O(log n).

## Approach
Standard binary search assumes full sortedness, which is broken here — but at least one half of any given subarray (from low to mid, or mid to high) is always fully sorted, even in a rotated array. Determine which half is sorted by comparing nums[low] to nums[mid], then check if the target falls within that sorted half's range to decide which side to recurse into.

## Complexity
- Time: O(log n) — still halves the search space each step, just with an extra sorted-half check.
- Space: O(1) iterative.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
