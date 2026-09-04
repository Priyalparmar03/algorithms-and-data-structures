# Container With Most Water

**Source:** LeetCode #11
**Topic:** Arrays
**Difficulty:** Medium

## Problem
Given heights of vertical lines at each index, find two lines that together with the x-axis form a container holding the most water.

## Approach
Brute force checks every pair — O(n²). Two pointers starting at both ends does better: the container's width is maximized at the ends, and its height is capped by the *shorter* line. Move the pointer at the shorter line inward, since moving the taller one can only decrease or keep width without ever increasing the limiting height. Track the best area seen.

## Complexity
- Time: O(n) — each pointer moves at most n times total.
- Space: O(1).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
