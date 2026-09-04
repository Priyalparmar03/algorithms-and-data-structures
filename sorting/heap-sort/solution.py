"""Heap Sort — build max-heap, then repeatedly extract the max in place."""
from typing import List


def heap_sort(nums: List[int]) -> List[int]:
    nums = nums.copy()
    n = len(nums)

    for i in range(n // 2 - 1, -1, -1):
        _heapify(nums, n, i)

    for end in range(n - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        _heapify(nums, end, 0)

    return nums


def _heapify(nums: List[int], size: int, root: int) -> None:
    largest = root
    left, right = 2 * root + 1, 2 * root + 2
    if left < size and nums[left] > nums[largest]:
        largest = left
    if right < size and nums[right] > nums[largest]:
        largest = right
    if largest != root:
        nums[root], nums[largest] = nums[largest], nums[root]
        _heapify(nums, size, largest)
