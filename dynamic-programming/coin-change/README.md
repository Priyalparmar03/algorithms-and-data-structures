# Coin Change

**Source:** LeetCode #322
**Topic:** Dynamic Programming
**Difficulty:** Medium

## Problem
Given coin denominations and a target amount, find the fewest number of coins needed to make that amount (or -1 if impossible).

## Approach
This is unbounded knapsack framing: for each amount from 1 up to the target, try every coin denomination and take the minimum of (1 + dp[amount - coin]) across all coins that fit. Bottom-up table building avoids the redundant recomputation that plain recursion would hit (the same sub-amounts get needed repeatedly from different paths).

## Complexity
- Time: O(amount * num_coins) — for each amount, try every coin.
- Space: O(amount) — the DP table.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
