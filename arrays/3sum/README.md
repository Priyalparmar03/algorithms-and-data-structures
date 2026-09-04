# 3Sum

**Source:** LeetCode #15
**Topic:** Arrays
**Difficulty:** Medium

## Problem
Given an array of integers, find all unique triplets that sum to zero.

## Approach
Brute force is O(n³). Sort the array first, then for each element, use two pointers on the remaining sorted subarray to find pairs summing to its negation — this reduces the inner search to O(n). Skip duplicate values at each level to avoid duplicate triplets in the output.

## Complexity
- Time: O(n²) — O(n log n) sort + O(n) outer loop × O(n) two-pointer scan.
- Space: O(1) extra (excluding output and sort space).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
