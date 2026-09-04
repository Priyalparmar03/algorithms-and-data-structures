# Longest Increasing Subsequence

**Source:** LeetCode #300
**Topic:** Dynamic Programming
**Difficulty:** Medium

## Problem
Given an array of integers, find the length of the longest strictly increasing subsequence.

## Approach
O(n²) DP: dp[i] = length of the longest increasing subsequence ending exactly at index i. For each i, check every earlier index j; if nums[j] < nums[i], the subsequence ending at j can be extended by nums[i]. The answer is the max over all dp[i]. (A faster O(n log n) version exists using binary search on a 'patience sorting' auxiliary array — included as a reflection, not the primary implementation, to keep the core DP idea clear first.)

## Complexity
- Time: O(n²) — for each index, scan all earlier indices.
- Space: O(n) — the DP array.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
The O(n log n) version maintains a 'tails' array (smallest tail value for each achievable subsequence length) and binary searches it for each new number — worth implementing as a follow-up to show the DP-to-greedy-plus-binary-search upgrade path explicitly.
