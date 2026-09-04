# 0 1 Knapsack

**Source:** Classic / GeeksforGeeks
**Topic:** Dynamic Programming
**Difficulty:** Medium

## Problem
Given item weights, values, and a knapsack capacity, maximize total value without exceeding capacity, using each item at most once (0/1 — take it or don't).

## Approach
dp[i][w] represents the best value achievable using the first i items with capacity w. For each item, choose the better of skipping it (dp[i-1][w]) or taking it (its value plus dp[i-1][w - its weight], only valid if it fits). The 'at most once' constraint is what distinguishes this from coin-change's unbounded version — iterating weight in the right order matters if space-optimizing to 1D.

## Complexity
- Time: O(n * capacity) — n items, capacity+1 weight values per item.
- Space: O(n * capacity) for the 2D table (optimizable to O(capacity) with a 1D array, iterating weight in reverse).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
