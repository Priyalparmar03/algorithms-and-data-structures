# Binary Tree Level Order Traversal

**Source:** LeetCode #102
**Topic:** Trees
**Difficulty:** Medium

## Problem
Return the level-order traversal of a binary tree's node values (i.e., left to right, level by level).

## Approach
This is BFS on a tree using a queue. Process one full level at a time: record the current queue size before the inner loop, pop exactly that many nodes (that's one level), collect their values, and push their children for the next iteration.

## Complexity
- Time: O(n) — every node enqueued/dequeued once.
- Space: O(n) — queue can hold up to the widest level, plus the output.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
