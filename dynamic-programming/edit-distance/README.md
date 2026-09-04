# Edit Distance

**Source:** LeetCode #72
**Topic:** Dynamic Programming
**Difficulty:** Hard

## Problem
Given two strings, find the minimum number of operations (insert, delete, replace) to convert one into the other.

## Approach
2D DP: dp[i][j] = min edits to convert the first i characters of word1 into the first j characters of word2. If the current characters match, no edit needed at this position (dp[i-1][j-1]). Otherwise, take the minimum of insert (dp[i][j-1] + 1), delete (dp[i-1][j] + 1), or replace (dp[i-1][j-1] + 1). Base cases: converting to/from an empty string costs exactly the length of the other string (all inserts or all deletes).

## Complexity
- Time: O(m * n) — fills an m x n table.
- Space: O(m * n) — the DP table (optimizable to O(min(m,n)) with two rows).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
