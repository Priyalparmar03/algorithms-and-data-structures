# Bubble Sort

**Source:** Classic
**Topic:** Sorting
**Difficulty:** Easy

## Problem
Implement bubble sort: repeatedly step through the array, swapping adjacent elements that are out of order.

## Approach
Repeated passes 'bubble' the largest unsorted element to its correct position at the end each time. Add an early-exit flag: if a full pass makes no swaps, the array is already sorted and further passes are unnecessary — this gives a best case of O(n) on already-sorted input instead of always running the full O(n²).

## Complexity
- Time: O(n²) average/worst case, O(n) best case (already sorted, with the early-exit optimization).
- Space: O(1) — in place.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
Bubble sort is rarely used in practice (insertion sort dominates it for small/nearly-sorted inputs), but implementing it correctly with the early-exit optimization is a good baseline to compare merge/quick sort against in complexity discussions.
