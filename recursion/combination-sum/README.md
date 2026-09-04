# Combination Sum

**Source:** LeetCode #39
**Topic:** Recursion
**Difficulty:** Medium

## Problem
Given an array of distinct positive integers (candidates) and a target, return all unique combinations where the chosen numbers sum to target. The same number may be reused unlimited times.

## Approach
Backtracking with a 'start index' that does NOT advance when a number is reused (allowing repeats) but DOES advance when moving past a number entirely — this distinguishes it from permutations/subsets which never reuse elements. Prune early whenever the running sum exceeds the target, which cuts off a large amount of unnecessary recursion.

## Complexity
- Time: O(n^(target/min_candidate)) — exponential in the worst case, bounded by how many times the smallest candidate can be reused, though pruning cuts this significantly in practice.
- Space: O(target / min_candidate) — recursion depth.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
