# Heap Sort

**Source:** Classic
**Topic:** Sorting
**Difficulty:** Medium

## Problem
Implement heap sort: build a max-heap from the array, then repeatedly extract the max element to build the sorted result.

## Approach
First build a max-heap in place via heapify (bottom-up, O(n) total, not O(n log n), by a classic amortized argument). Then repeatedly swap the heap's root (the max) with the last unsorted element, shrink the heap by one, and re-heapify from the root — this places the largest remaining element correctly at the end of the array each time.

## Complexity
- Time: O(n log n) — O(n) to build the heap, then n extractions each costing O(log n) to re-heapify.
- Space: O(1) — sorts in place, no auxiliary array.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
Heap sort's O(1) space is a real advantage over merge sort's O(n), but it's not stable (equal elements can be reordered) and has worse cache locality than quicksort in practice — good talking point on why 'better big-O' doesn't always mean 'better in practice.'
