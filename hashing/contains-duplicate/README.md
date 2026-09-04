# Contains Duplicate

**Source:** LeetCode #217
**Topic:** Hashing
**Difficulty:** Easy

## Problem
Given an array of integers, determine if any value appears at least twice.

## Approach
A hash set naturally tracks 'have I seen this before' in O(1) per lookup — either build the full set and compare its size to the array length, or (slightly better, early-exits on the first duplicate) insert one at a time and return True the moment an insert finds an existing value.

## Complexity
- Time: O(n) — single pass.
- Space: O(n) — hash set can hold up to n elements.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
