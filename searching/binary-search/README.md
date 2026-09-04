# Binary Search

**Source:** LeetCode #704
**Topic:** Searching
**Difficulty:** Easy

## Problem
Given a sorted array and a target value, return its index, or -1 if not found.

## Approach
Repeatedly halve the search space: compare the target to the middle element, and discard the half that can't contain it. This only works because the array is sorted — the halving is what gets this to logarithmic time instead of linear.

## Complexity
- Time: O(log n) — search space halves each iteration.
- Space: O(1) iterative.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
`(low + high) // 2` can overflow in languages with fixed-width integers (not a concern in Python) — the safer general form is `low + (high - low) // 2`, worth mentioning if this comes up in a language-agnostic interview context.
