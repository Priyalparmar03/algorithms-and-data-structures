# Best Time To Buy Sell Stock

**Source:** LeetCode #121
**Topic:** Arrays
**Difficulty:** Easy

## Problem
Given an array `prices` where prices[i] is the stock price on day i, find the maximum profit from a single buy followed by a single sell (buy must happen before sell).

## Approach
Brute force checks every buy/sell pair — O(n²). Instead, scan once tracking the minimum price seen so far. At each day, the best possible profit if you sold today is price - min_so_far. Track the max of that as you go. This works because you only ever need the lowest price *before* the current day, not all pairs.

## Complexity
- Time: O(n) — single pass.
- Space: O(1) — two running variables.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
A sliding-window / two-pointer framing also works but the running-minimum approach is simpler to reason about and generalizes less cleanly to the 'multiple transactions' variant of this problem.
