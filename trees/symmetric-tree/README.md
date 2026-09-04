# Symmetric Tree

**Source:** LeetCode #101
**Topic:** Trees
**Difficulty:** Easy

## Problem
Check whether a binary tree is a mirror of itself (symmetric around its center).

## Approach
A tree is symmetric if its left and right subtrees are mirror images of each other. Write a helper that compares two subtrees as mirrors: their root values must match, the left subtree's left must mirror the right subtree's right, and the left subtree's right must mirror the right subtree's left. Recurse with that swapped pairing.

## Complexity
- Time: O(n) — visits every node once.
- Space: O(h) — recursion stack.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
