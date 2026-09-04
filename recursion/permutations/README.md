# Permutations

**Source:** LeetCode #46
**Topic:** Recursion
**Difficulty:** Medium

## Problem
Given an array of unique integers, return all possible permutations.

## Approach
Backtracking that builds one permutation at a time: at each step, try every unused number as the next element, recurse, then undo (backtrack) before trying the next option. A 'used' boolean array (or checking membership in the current partial permutation) prevents reusing an element already placed.

## Complexity
- Time: O(n! * n) — n! permutations, each up to O(n) to copy into the result.
- Space: O(n) — recursion depth plus the used-tracking array.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
