# Validate Binary Search Tree

**Source:** LeetCode #98
**Topic:** Trees
**Difficulty:** Medium

## Problem
Determine if a binary tree is a valid binary search tree (BST).

## Approach
A common bug is only checking each node against its immediate children — that misses violations from ancestors further up. Instead, pass down a valid (low, high) range as you recurse: each node must fall strictly within the range established by all its ancestors, and it narrows the range for its own children.

## Complexity
- Time: O(n) — visits every node once.
- Space: O(h) — recursion stack.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
This problem is a good example of why 'compare each node to its parent' is a common wrong-but-plausible solution — the range-propagation approach is the correct generalization.
