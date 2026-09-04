# Reorder List

**Source:** LeetCode #143
**Topic:** Linked Lists
**Difficulty:** Medium

## Problem
Given a linked list L0-L1-...-Ln, reorder it in place to L0-Ln-L1-Ln-1-L2-Ln-2-....

## Approach
Three-step combination: (1) find the middle using slow/fast pointers, (2) reverse the second half of the list, (3) merge the two halves by alternating nodes. Each step is a pattern seen in earlier problems (cycle detection's slow/fast, reverse-linked-list) composed together.

## Complexity
- Time: O(n) — three linear passes.
- Space: O(1) — everything done via pointer rewiring.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
