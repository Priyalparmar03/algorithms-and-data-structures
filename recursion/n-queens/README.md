# N Queens

**Source:** LeetCode #51
**Topic:** Recursion
**Difficulty:** Hard

## Problem
Place n queens on an n x n chessboard so that no two queens attack each other (same row, column, or diagonal). Return all distinct solutions.

## Approach
Backtracking, placing one queen per row (this guarantees no two queens ever share a row automatically). At each row, try every column; before placing, check that the column and both diagonals aren't already under attack from previously placed queens. Track occupied columns and diagonals with sets for O(1) conflict checks instead of re-scanning the whole board.

## Complexity
- Time: O(n!) roughly — pruned heavily in practice by the conflict checks, much better than the naive O(n^n) of trying every placement without pruning.
- Space: O(n) — recursion depth plus the column/diagonal tracking sets.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
