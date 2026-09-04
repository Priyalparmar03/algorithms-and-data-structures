# Subsets

**Source:** LeetCode #78
**Topic:** Recursion
**Difficulty:** Medium

## Problem
Given an array of unique integers, return all possible subsets (the power set).

## Approach
Classic include/exclude backtracking: for each element, recursively branch into two paths — one where it's included in the current subset, one where it's excluded. At the end of the array, whatever subset has been built is added to the result. This produces exactly 2^n subsets, matching the size of the power set.

## Complexity
- Time: O(2^n * n) — 2^n subsets, each up to O(n) to copy into the result.
- Space: O(n) — recursion depth (excluding output storage).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
