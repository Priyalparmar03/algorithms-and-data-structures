# Maximum Depth Of Binary Tree

**Source:** LeetCode #104
**Topic:** Trees
**Difficulty:** Easy

## Problem
Given the root of a binary tree, return its maximum depth (number of nodes along the longest path from root to a leaf).

## Approach
Classic recursion: the depth of a tree is 1 (for the root) plus the max depth of its left and right subtrees. Base case: an empty tree has depth 0. This is the simplest possible tree recursion and a good template for more complex tree DFS problems.

## Complexity
- Time: O(n) — visits every node once.
- Space: O(h) — recursion stack depth equals tree height (worst case O(n) for a skewed tree, O(log n) for a balanced one).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
