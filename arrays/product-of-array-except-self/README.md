# Product Of Array Except Self

**Source:** LeetCode #238
**Topic:** Arrays
**Difficulty:** Medium

## Problem
Given an array `nums`, return an array `answer` where answer[i] is the product of all elements except nums[i], without using division and in O(n) time.

## Approach
Without division, compute prefix products (product of everything to the left of i) and suffix products (product of everything to the right of i) separately, then multiply them. Do this in two passes reusing the output array for prefixes, then a single running suffix variable instead of a second array to keep space at O(1) extra (excluding the output).

## Complexity
- Time: O(n) — two passes.
- Space: O(1) extra space (output array doesn't count).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
