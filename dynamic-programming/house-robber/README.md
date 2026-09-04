# House Robber

**Source:** LeetCode #198
**Topic:** Dynamic Programming
**Difficulty:** Medium

## Problem
Given an array of non-negative integers representing money in houses along a street, find the max amount you can rob without robbing two adjacent houses.

## Approach
At each house, there's a choice: skip it (carry forward the best result up to the previous house), or rob it (its value plus the best result up to two houses back, since the adjacent one can't also be robbed). dp[i] = max(dp[i-1], dp[i-2] + nums[i]). Only the last two DP values are ever needed, so space collapses to O(1).

## Complexity
- Time: O(n) — single pass.
- Space: O(1) — two running variables (space-optimized from an O(n) DP array).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
