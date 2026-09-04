"""Find Peak Element — binary search exploiting local slope, not sortedness."""
from typing import List


def find_peak_element(nums: List[int]) -> int:
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < nums[mid + 1]:
            low = mid + 1  # peak is to the right
        else:
            high = mid      # peak is at mid or to the left
    return low
