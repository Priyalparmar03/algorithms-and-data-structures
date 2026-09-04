"""Median of Two Sorted Arrays — binary search on partition point, no merging."""
from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    low, high = 0, m
    half = (m + n + 1) // 2

    while low <= high:
        i = (low + high) // 2
        j = half - i

        left_a = nums1[i - 1] if i > 0 else float("-inf")
        right_a = nums1[i] if i < m else float("inf")
        left_b = nums2[j - 1] if j > 0 else float("-inf")
        right_b = nums2[j] if j < n else float("inf")

        if left_a <= right_b and left_b <= right_a:
            if (m + n) % 2 == 1:
                return max(left_a, left_b)
            return (max(left_a, left_b) + min(right_a, right_b)) / 2
        elif left_a > right_b:
            high = i - 1
        else:
            low = i + 1

    raise ValueError("Input arrays are not sorted")
