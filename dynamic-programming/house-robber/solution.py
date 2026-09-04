"""House Robber — DP choosing skip vs. rob at each house, O(1) space."""
from typing import List


def rob(nums: List[int]) -> int:
    prev2, prev1 = 0, 0
    for num in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + num)
    return prev1
