# Group Anagrams

**Source:** LeetCode #49
**Topic:** Hashing
**Difficulty:** Medium

## Problem
Given an array of strings, group the anagrams together.

## Approach
Two strings are anagrams iff their sorted character sequences are identical, so that sorted string makes a perfect hash-map key. Map each word's sorted form to a list of original words sharing that form; one pass builds the groups.

## Complexity
- Time: O(n * k log k) — n words, each sorted in O(k log k) where k is word length.
- Space: O(n * k) — storing all words in the map.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
A character-count tuple (26-length array of letter frequencies) as the key avoids the O(k log k) sort, giving O(n*k) total — worth using instead when word lengths are large.
