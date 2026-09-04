"""Rotate Array — reverse-based in-place rotation."""
from typing import List


def rotate(nums: List[int], k: int) -> None:
    n = len(nums)
    k %= n
    _reverse(nums, 0, n - 1)
    _reverse(nums, 0, k - 1)
    _reverse(nums, k, n - 1)


def _reverse(nums: List[int], lo: int, hi: int) -> None:
    while lo < hi:
        nums[lo], nums[hi] = nums[hi], nums[lo]
        lo += 1
        hi -= 1
