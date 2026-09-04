# Merge Sort

**Source:** Classic
**Topic:** Sorting
**Difficulty:** Medium

## Problem
Implement merge sort: a divide-and-conquer sort that recursively splits the array in half, sorts each half, then merges the two sorted halves.

## Approach
Split the array until subarrays have length 1 (trivially sorted), then merge pairs of sorted subarrays back together, always taking the smaller of the two current front elements. The merge step is what does the actual work — the recursion just gets you down to a base case. Guaranteed O(n log n) regardless of input order, unlike quicksort's worst case.

## Complexity
- Time: O(n log n) — always, in every case (best/average/worst).
- Space: O(n) — auxiliary arrays for merging.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
Merge sort's guaranteed O(n log n) and stability (equal elements keep relative order) make it the right choice when worst-case time matters or when sorting objects by one field while preserving order on ties — quicksort trades that guarantee for typically better constant factors.
