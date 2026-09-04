# Longest Consecutive Sequence

**Source:** LeetCode #128
**Topic:** Hashing
**Difficulty:** Medium

## Problem
Given an unsorted array of integers, find the length of the longest run of consecutive integers, in O(n) time.

## Approach
Put all numbers in a hash set for O(1) lookup. For each number, only start counting a sequence if (num - 1) is NOT in the set — that means num is a sequence's start. From there, count upward (num+1, num+2, ...) while values exist in the set. This 'only start at true sequence starts' check is what keeps the total work O(n) instead of O(n²), since each number is only ever the start of at most one counted sequence.

## Complexity
- Time: O(n) — each number is visited by the inner while-loop at most once across the whole run.
- Space: O(n) — the hash set.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
