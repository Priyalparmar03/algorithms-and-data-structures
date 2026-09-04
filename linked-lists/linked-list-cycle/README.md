# Linked List Cycle

**Source:** LeetCode #141
**Topic:** Linked Lists
**Difficulty:** Easy

## Problem
Determine if a linked list has a cycle.

## Approach
Floyd's Tortoise and Hare: use two pointers, one moving one step at a time (slow) and one moving two steps at a time (fast). If there's a cycle, the fast pointer will eventually lap the slow pointer and they'll meet inside the cycle. If there's no cycle, fast reaches the end (None) first.

## Complexity
- Time: O(n) — fast pointer traverses at most twice the list length before meeting slow or reaching the end.
- Space: O(1) — only two pointers, no extra structure.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
A hash-set-of-visited-nodes approach also works and is arguably more intuitive, but costs O(n) space — Floyd's is the answer to give when the interviewer asks for O(1) space specifically.
