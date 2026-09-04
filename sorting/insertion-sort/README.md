# Insertion Sort

**Source:** Classic
**Topic:** Sorting
**Difficulty:** Easy

## Problem
Implement insertion sort: build the sorted array one element at a time by inserting each new element into its correct position among the already-sorted prefix.

## Approach
Maintain a growing sorted prefix. For each new element, shift larger elements in the sorted prefix one position to the right until the correct insertion point is found, then place the element there. This is efficient for small or nearly-sorted arrays since the inner shifting loop does very little work when elements are already close to their correct position.

## Complexity
- Time: O(n²) average/worst case, O(n) best case (nearly sorted input).
- Space: O(1) — in place.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
This is the algorithm many production sort implementations (like Timsort/Python's sort) fall back to for small subarrays, since its low constant factor beats merge/quick sort's overhead below a certain size threshold.
