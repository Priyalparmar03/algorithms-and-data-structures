# Two Sum

**Source:** LeetCode #1
**Topic:** Arrays / Hashing
**Difficulty:** Easy

## Problem
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. Assume exactly one solution exists, and you may not use the same element twice.

Edge cases: negative numbers, duplicate values in the array, target achieved by two identical values at different indices.

## Approach
Brute force checks every pair — O(n²) time, O(1) space. That's wasteful because for each element we already know what value we *need* (target - current), so instead of searching for it, we can look it up.

Insight: use a hash map to store each value's index as we scan. For each new number, check if its complement (target - num) is already in the map. If yes, we've found the pair in one pass. If no, add the current number to the map and continue.

## Complexity
- Time: O(n) — single pass, O(1) average-case hash map lookup/insert per element.
- Space: O(n) — worst case every element is stored before a match is found.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`. Covers: standard case, negative numbers, duplicate values, target found at last pair.

## Reflection
The sorted-two-pointer approach gives O(n log n) time but O(1) extra space (excluding output) — worth using instead if memory is constrained and returning indices isn't required, since sorting loses the original indices.
