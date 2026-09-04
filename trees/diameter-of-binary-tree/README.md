# Diameter Of Binary Tree

**Source:** LeetCode #543
**Topic:** Trees
**Difficulty:** Easy

## Problem
Find the length (in edges) of the longest path between any two nodes in a binary tree — the path doesn't have to pass through the root.

## Approach
The key insight: the longest path through any given node equals the sum of the left and right subtree heights at that node. Compute subtree height recursively as normal, but as a side effect, update a running 'best diameter' at every node using left_height + right_height, since the answer might peak at any node, not just the root.

## Complexity
- Time: O(n) — each node visited once, height and diameter computed together in one pass.
- Space: O(h) — recursion stack.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
A naive version recomputes height() separately for every node when checking the diameter at each point, giving O(n²). Combining the height computation and the diameter update into one traversal is what gets this to O(n) — worth calling out explicitly since the naive version is a very natural first attempt.
