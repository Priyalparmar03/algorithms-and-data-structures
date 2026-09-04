# Palindrome Linked List

**Source:** LeetCode #234
**Topic:** Linked Lists
**Difficulty:** Easy

## Problem
Determine whether a singly linked list is a palindrome.

## Approach
The simplest approach copies values into an array and checks it reads the same forward and backward (O(n) space). The O(1)-space version: find the middle (slow/fast pointers), reverse the second half in place, then compare the first half against the reversed second half node-by-node.

## Complexity
- Time: O(n) — linear passes to find middle, reverse, and compare.
- Space: O(1) with the reverse-in-place approach (O(n) with the array approach).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
The O(1)-space approach mutates the list during the check (reverses second half) — mention in an interview that you'd restore it afterward if the list must stay unmodified for the caller.
