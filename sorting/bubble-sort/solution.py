"""Bubble Sort — with early-exit optimization for already-sorted input."""
from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    nums = nums.copy()
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums
