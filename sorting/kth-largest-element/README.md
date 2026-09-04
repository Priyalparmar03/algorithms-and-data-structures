# Kth Largest Element

**Source:** LeetCode #215
**Topic:** Sorting
**Difficulty:** Medium

## Problem
Find the kth largest element in an unsorted array (not the kth distinct element).

## Approach
Full sorting is O(n log n) but wasteful when you only need one element. Quickselect (partition-based, same partition step as quicksort) finds the kth largest in average O(n): after partitioning around a pivot, the pivot's final index tells you exactly how many elements are larger than it, so you can recurse into only the relevant side instead of both.

## Complexity
- Time: O(n) average case (Quickselect), O(n²) worst case with poor pivot choices.
- Space: O(1) — in place (excluding recursion stack).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
A min-heap of size k is a simpler-to-reason-about alternative giving O(n log k) — worth mentioning as the answer when an interviewer specifically asks for a streaming/online version where you don't have the whole array in memory at once.
