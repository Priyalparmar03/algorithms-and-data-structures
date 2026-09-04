# Maximum Subarray

**Source:** LeetCode #53
**Topic:** Arrays
**Difficulty:** Medium

## Problem
Given an integer array, find the contiguous subarray with the largest sum and return that sum.

## Approach
Brute force checks all O(n²) subarrays. Kadane's algorithm instead asks, at each position: is it better to extend the previous subarray, or start fresh here? If the running sum so far is negative, it can only hurt future sums, so drop it and start over from the current element. Track the max seen at every step.

## Complexity
- Time: O(n) — single pass.
- Space: O(1) — two running variables.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
This is a good problem to explain in interviews via the DP lens too: current = max(nums[i], dp[i-1] + nums[i]) — Kadane's is really a space-optimized 1D DP.
