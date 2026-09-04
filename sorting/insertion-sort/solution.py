"""Insertion Sort."""
from typing import List


def insertion_sort(nums: List[int]) -> List[int]:
    nums = nums.copy()
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums
