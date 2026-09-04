# Median Of Two Sorted Arrays

**Source:** LeetCode #4
**Topic:** Searching
**Difficulty:** Hard

## Problem
Given two sorted arrays, find the median of the combined array in O(log(min(m,n))) time.

## Approach
Merging both arrays would be O(m+n), too slow for the required complexity. Instead, binary search on the *partition point* of the smaller array: for any partition of array A, there's a corresponding partition of array B such that the left halves combined have exactly half the total elements. Binary search for the A-partition where max(left) <= min(right) holds on both sides — that partition point directly gives the median without ever merging.

## Complexity
- Time: O(log(min(m, n))) — binary search only on the smaller array's partition points.
- Space: O(1).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
This is the hardest problem in the whole repo, included deliberately — it demonstrates the difference between 'binary search on a value' (most other problems here) and 'binary search on an answer/partition structure,' a more advanced pattern worth being able to explain the reasoning behind, not just the code.
