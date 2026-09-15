# Rotate Array

**Source:** LeetCode #189
**Topic:** Arrays
**Difficulty:** Medium

C++ Solution : https://leetcode.com/problems/rotate-array/submissions/2142811430/

## Problem
Rotate an array to the right by k steps, in place.

## Approach
A naive approach rotates one step at a time k times — O(nk). The clean O(n) in-place trick: reverse the whole array, then reverse the first k elements, then reverse the remaining n-k elements. Three reversals compose into exactly the rotation you want.

## Complexity
- Time: O(n) — three linear reversal passes.
- Space: O(1) — in place.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
