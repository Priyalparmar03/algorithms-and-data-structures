# Remove Nth Node From End

**Source:** LeetCode #19
**Topic:** Linked Lists
**Difficulty:** Medium

## Problem
Remove the nth node from the end of a linked list, in one pass, and return the head.

## Approach
Use two pointers with a fixed gap of n between them. Advance a 'fast' pointer n steps ahead first, then move both fast and 'slow' together until fast hits the end — at that point slow is right before the node to remove. A dummy head handles the edge case of removing the head itself cleanly.

## Complexity
- Time: O(n) — single pass with two pointers.
- Space: O(1).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
