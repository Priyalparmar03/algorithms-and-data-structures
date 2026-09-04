"""Subarray Sum Equals K — prefix sum counts in a hash map."""
from collections import defaultdict
from typing import List


def subarray_sum(nums: List[int], k: int) -> int:
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1  # empty prefix
    running_sum = 0
    count = 0
    for num in nums:
        running_sum += num
        count += prefix_counts[running_sum - k]
        prefix_counts[running_sum] += 1
    return count
