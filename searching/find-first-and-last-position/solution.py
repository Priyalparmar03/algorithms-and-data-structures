"""Find First and Last Position — two biased binary searches."""
from typing import List


def search_range(nums: List[int], target: int) -> List[int]:
    return [_find_bound(nums, target, find_first=True), _find_bound(nums, target, find_first=False)]


def _find_bound(nums: List[int], target: int, find_first: bool) -> int:
    low, high = 0, len(nums) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            result = mid
            if find_first:
                high = mid - 1  # keep searching left
            else:
                low = mid + 1   # keep searching right
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result
