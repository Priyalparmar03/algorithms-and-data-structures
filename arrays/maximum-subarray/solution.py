"""Maximum Subarray — Kadane's algorithm."""
from typing import List


def max_subarray(nums: List[int]) -> int:
    best = current = nums[0]
    for n in nums[1:]:
        current = max(n, current + n)
        best = max(best, current)
    return best
