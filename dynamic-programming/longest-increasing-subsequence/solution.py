"""Longest Increasing Subsequence — O(n^2) DP (patience-sorting O(n log n) noted in README)."""
from typing import List


def length_of_lis(nums: List[int]) -> int:
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
