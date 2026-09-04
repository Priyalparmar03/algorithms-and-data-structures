# Isomorphic Strings

**Source:** LeetCode #205
**Topic:** Hashing
**Difficulty:** Easy

## Problem
Given two strings s and t, determine if they are isomorphic (characters in s can be consistently replaced to get t, with a one-to-one mapping in both directions).

## Approach
A one-directional character map isn't enough — 'ab' -> 'aa' would incorrectly pass a naive s-to-t-only check. Maintain two hash maps, one for the s-to-t mapping and one for t-to-s, and verify both directions stay consistent at every position. This enforces the bijection (one-to-one, not just many-to-one).

## Complexity
- Time: O(n) — single pass.
- Space: O(k) — k distinct characters, bounded by alphabet size.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
