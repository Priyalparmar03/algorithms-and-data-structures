# Longest Common Subsequence

**Source:** LeetCode #1143
**Topic:** Dynamic Programming
**Difficulty:** Medium

## Problem
Given two strings, find the length of their longest common subsequence (characters in the same relative order, not necessarily contiguous).

## Approach
Classic 2D DP: dp[i][j] represents the LCS length of the first i characters of s1 and first j characters of s2. If the current characters match, extend the diagonal (dp[i-1][j-1] + 1); otherwise take the best of dropping a character from either string (max(dp[i-1][j], dp[i][j-1])). Build the table bottom-up from the empty-string base case.

## Complexity
- Time: O(m * n) — fills an m x n table, one O(1) computation per cell.
- Space: O(m * n) — the DP table (can be optimized to O(min(m,n)) by keeping only two rows).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
