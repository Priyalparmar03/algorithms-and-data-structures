# Counting Sort

**Source:** Classic
**Topic:** Sorting
**Difficulty:** Easy

## Problem
Implement counting sort for an array of non-negative integers with a known small range.

## Approach
When the range of possible values (k) is small relative to n, counting sort beats any comparison-based sort's O(n log n) lower bound by not comparing elements at all: count occurrences of each value in a bucket array, then reconstruct the sorted output by reading off counts in order. This only works for integers (or values mappable to small integer keys) with a bounded range — it's not a general-purpose sort.

## Complexity
- Time: O(n + k) — n elements, k = range of values.
- Space: O(n + k) — count array plus output array.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
Counting sort assumes non-negative integers with a small max value — it would blow up in memory on something like [1, 1_000_000_000], where a comparison sort would still be O(n log n) regardless of value magnitude. Worth stating this limitation explicitly, since 'faster than O(n log n)' sounds like a free upgrade until you hit that case.
