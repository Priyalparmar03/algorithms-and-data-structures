# Merge Two Sorted Lists

**Source:** LeetCode #21
**Topic:** Linked Lists
**Difficulty:** Easy

## Problem
Merge two sorted linked lists into one sorted linked list by splicing the existing nodes together.

## Approach
Use a dummy head node to simplify edge cases, then walk both lists with two pointers, always attaching the smaller current node to the result and advancing that list's pointer. When one list runs out, attach the remainder of the other directly — it's already sorted.

## Complexity
- Time: O(n + m) — each node visited once.
- Space: O(1) extra — nodes are relinked, not copied.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
