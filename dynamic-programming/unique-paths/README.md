# Unique Paths

**Source:** LeetCode #62
**Topic:** Dynamic Programming
**Difficulty:** Medium

## Problem
A robot on an m x n grid starts at the top-left and can only move right or down. How many unique paths exist to the bottom-right corner?

## Approach
dp[r][c] = number of ways to reach cell (r, c). Since the robot can only arrive from above or from the left, dp[r][c] = dp[r-1][c] + dp[r][c-1]. The first row and first column are base cases with exactly 1 path each (only one direction of travel is possible along an edge).

## Complexity
- Time: O(m * n) — fills the grid once.
- Space: O(m * n) for the 2D table (optimizable to O(n) using a single 1D row, updated in place).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
This is a combinatorics problem in disguise -- the closed-form answer is C(m+n-2, m-1) (choose which of the m+n-2 total moves are 'down'). Knowing the DP solution is more generally useful (it extends easily to grids with obstacles, where the closed form breaks), but recognizing the shortcut shows deeper understanding.
