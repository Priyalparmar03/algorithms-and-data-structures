# Path Sum

**Source:** LeetCode #112
**Topic:** Trees
**Difficulty:** Easy

## Problem
Given a binary tree and a target sum, determine if the tree has a root-to-leaf path where the values along the path add up to the target.

## Approach
DFS while subtracting each node's value from the remaining target as you descend. At a leaf, check whether the remaining target has been reduced to exactly 0. This avoids building and storing full path lists — you only need the running remainder.

## Complexity
- Time: O(n) — worst case visits every node.
- Space: O(h) — recursion stack.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
