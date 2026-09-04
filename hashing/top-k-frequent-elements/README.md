# Top K Frequent Elements

**Source:** LeetCode #347
**Topic:** Hashing
**Difficulty:** Medium

## Problem
Given an array of integers, return the k most frequent elements.

## Approach
Count frequencies with a hash map, then avoid a full O(n log n) sort by using bucket sort: create buckets indexed by frequency (1 to n), place each number in the bucket matching its count, then read off the top k by scanning buckets from highest frequency downward. This gets the whole thing to linear time.

## Complexity
- Time: O(n) — counting is O(n), bucket sort avoids the O(n log n) comparison sort.
- Space: O(n) — frequency map plus buckets.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
A heap-based approach (heapq.nlargest) is simpler to write and gives O(n log k), which is actually better than bucket sort's O(n) only in the constant factor for small k — worth knowing both, since interviewers sometimes push for the heap version first.
