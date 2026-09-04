# Lowest Common Ancestor Bst

**Source:** LeetCode #235
**Topic:** Trees
**Difficulty:** Medium

## Problem
Given a BST and two nodes p and q, find their lowest common ancestor (LCA).

## Approach
A BST's ordering gives a shortcut over general-tree LCA: starting at the root, if both p and q's values are less than the current node, the LCA must be in the left subtree; if both are greater, it's in the right subtree; otherwise (values split, or one equals the current node), the current node is the LCA — this is the split point.

## Complexity
- Time: O(h) — walks down one path, h = tree height.
- Space: O(1) iterative (O(h) if written recursively).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
