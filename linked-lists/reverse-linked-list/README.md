# Reverse Linked List

**Source:** LeetCode #206
**Topic:** Linked Lists
**Difficulty:** Easy

## Problem
Reverse a singly linked list and return the new head.

## Approach
Iterate through the list keeping three pointers: previous, current, and next. At each node, save its next pointer before overwriting it to point backward at previous, then advance all three pointers. This reverses the list in a single pass with no extra structure.

## Complexity
- Time: O(n) — single pass.
- Space: O(1) iterative (O(n) if done recursively, due to call stack).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
The recursive version is more elegant to write (reverse_list(head.next) then rewire) but trades O(1) space for O(n) call-stack space — worth mentioning explicitly, since 'looks cleaner' isn't the same as 'better complexity.'
