# Find Peak Element

**Source:** LeetCode #162
**Topic:** Searching
**Difficulty:** Medium

## Problem
Given an array where nums[i] != nums[i+1], find any peak element (greater than both neighbors) in O(log n). Boundaries count as -infinity.

## Approach
Binary search still applies here even though the array isn't sorted, because of a key property: if nums[mid] < nums[mid+1], a peak is guaranteed to exist somewhere to the right (since values are trending up), so search right; otherwise a peak is guaranteed on the left side (including mid itself). This 'guaranteed to exist in the discarded half's complement' reasoning is what makes binary search apply to unsorted-but-structured inputs.

## Complexity
- Time: O(log n) — halves the search space each step.
- Space: O(1).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
