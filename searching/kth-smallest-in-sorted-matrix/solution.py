"""Kth Smallest in a Sorted Matrix — binary search on value range + counting."""
from typing import List


def kth_smallest(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    low, high = matrix[0][0], matrix[n - 1][n - 1]

    while low < high:
        mid = (low + high) // 2
        count = _count_less_equal(matrix, mid, n)
        if count < k:
            low = mid + 1
        else:
            high = mid
    return low


def _count_less_equal(matrix: List[List[int]], target: int, n: int) -> int:
    count = 0
    row, col = n - 1, 0
    while row >= 0 and col < n:
        if matrix[row][col] <= target:
            count += row + 1
            col += 1
        else:
            row -= 1
    return count
