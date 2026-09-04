# Subarray Sum Equals K

**Source:** LeetCode #560
**Topic:** Hashing
**Difficulty:** Medium

## Problem
Given an array of integers and an integer k, find the total number of contiguous subarrays whose sum equals k.

## Approach
Brute force checks every subarray — O(n²). Instead track running prefix sums and use a hash map counting how many times each prefix sum value has occurred. A subarray (i, j] sums to k exactly when prefix[j] - prefix[i] == k, i.e. prefix[i] == prefix[j] - k — so at each position, look up how many earlier prefix sums equal (current prefix sum - k) and add that count to the answer.

## Complexity
- Time: O(n) — single pass with O(1) average hash map operations.
- Space: O(n) — hash map of prefix sum counts.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
The prefix_counts[0] = 1 initialization is the easy-to-miss detail here — without it, subarrays that sum to k starting from index 0 get silently undercounted.
