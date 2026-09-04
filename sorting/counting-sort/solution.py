"""Counting Sort — non-comparison sort for a small, known integer range."""
from typing import List


def counting_sort(nums: List[int]) -> List[int]:
    if not nums:
        return []
    max_val = max(nums)
    counts = [0] * (max_val + 1)
    for n in nums:
        counts[n] += 1

    result = []
    for value, count in enumerate(counts):
        result.extend([value] * count)
    return result
