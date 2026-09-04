# Quick Sort

**Source:** Classic
**Topic:** Sorting
**Difficulty:** Medium

## Problem
Implement quicksort: a divide-and-conquer sort that picks a pivot, partitions the array around it, and recursively sorts each partition.

## Approach
Choose a pivot (last element here, for simplicity), then partition in place: walk through the array, moving every element smaller than the pivot to the front, and finally place the pivot in its correct sorted position between the two partitions. Recurse on the left and right partitions independently. Average case is fast because partitions tend to be roughly balanced; worst case (already-sorted input with last-element pivot) degrades to O(n²) since partitions become maximally unbalanced.

## Complexity
- Time: O(n log n) average case, O(n²) worst case (bad pivot choices, e.g. already-sorted input with last-element pivot).
- Space: O(log n) average — recursion stack (O(n) worst case for unbalanced recursion).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
A random or median-of-three pivot choice instead of always the last element avoids the O(n²) worst case on already-sorted or reverse-sorted input — worth implementing as a follow-up to show awareness of this weakness.
