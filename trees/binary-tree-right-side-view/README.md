# Binary Tree Right Side View

**Source:** LeetCode #199
**Topic:** Trees
**Difficulty:** Medium

## Problem
Given a binary tree, return the values visible from the right side, ordered top to bottom.

## Approach
This is level-order BFS (as in binary-tree-level-order-traversal) where you only keep the last node processed at each level — that's the rightmost, hence visible-from-the-right, node.

## Complexity
- Time: O(n) — every node visited once.
- Space: O(n) — queue can hold up to the widest level.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
