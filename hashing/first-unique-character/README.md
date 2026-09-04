# First Unique Character

**Source:** LeetCode #387
**Topic:** Hashing
**Difficulty:** Easy

## Problem
Given a string, find the index of the first non-repeating character. Return -1 if none exists.

## Approach
Count all character frequencies in one pass, then scan the string a second time in original order and return the index of the first character whose count is exactly 1. Two linear passes beat any approach that re-scans the whole string per character.

## Complexity
- Time: O(n) — two linear passes.
- Space: O(1) — at most 26 keys for lowercase English letters.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
