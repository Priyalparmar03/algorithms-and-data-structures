# Valid Anagram

**Source:** LeetCode #242
**Topic:** Hashing
**Difficulty:** Easy

## Problem
Given two strings s and t, determine if t is an anagram of s.

## Approach
Count character frequencies in s using a hash map (or fixed-size array for lowercase letters), then decrement for each character in t. If any count goes negative or the final counts aren't all zero, they're not anagrams. Also a fast length mismatch check first as an early exit.

## Complexity
- Time: O(n) — single pass per string.
- Space: O(1) — at most 26 keys for lowercase English letters (O(k) in general for k distinct characters).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
