"""Kth Largest Element — Quickselect (partition-based selection)."""
import random
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    nums = nums.copy()
    target_index = len(nums) - k  # kth largest = index (n-k) in ascending sorted order
    return _quickselect(nums, 0, len(nums) - 1, target_index)


def _quickselect(nums: List[int], low: int, high: int, target: int) -> int:
    if low == high:
        return nums[low]
    pivot_index = random.randint(low, high)
    nums[pivot_index], nums[high] = nums[high], nums[pivot_index]
    pivot_index = _partition(nums, low, high)
    if pivot_index == target:
        return nums[pivot_index]
    elif pivot_index < target:
        return _quickselect(nums, pivot_index + 1, high, target)
    else:
        return _quickselect(nums, low, pivot_index - 1, target)


def _partition(nums: List[int], low: int, high: int) -> int:
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1
