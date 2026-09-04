# Add Two Numbers

**Source:** LeetCode #2
**Topic:** Linked Lists
**Difficulty:** Medium

## Problem
Two non-negative integers are represented as linked lists in reverse order (each node one digit). Add them and return the sum as a linked list in the same format.

## Approach
This mirrors elementary-school column addition: walk both lists simultaneously, adding corresponding digits plus any carry from the previous position, and creating a new node with the result digit mod 10. When one list is shorter, treat its missing digit as 0. Continue past both lists if there's a final carry.

## Complexity
- Time: O(max(n, m)) — one pass across the longer list.
- Space: O(max(n, m)) — for the output list.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
