"""Quick Sort — Lomuto partition scheme, last element as pivot."""
from typing import List


def quick_sort(nums: List[int]) -> List[int]:
    nums = nums.copy()
    _quick_sort(nums, 0, len(nums) - 1)
    return nums


def _quick_sort(nums: List[int], low: int, high: int) -> None:
    if low < high:
        pivot_index = _partition(nums, low, high)
        _quick_sort(nums, low, pivot_index - 1)
        _quick_sort(nums, pivot_index + 1, high)


def _partition(nums: List[int], low: int, high: int) -> int:
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1
