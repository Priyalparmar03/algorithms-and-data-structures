"""Longest Consecutive Sequence — hash set, only expand from true sequence starts."""
from typing import List


def longest_consecutive(nums: List[int]) -> int:
    num_set = set(nums)
    best = 0
    for num in num_set:
        if num - 1 not in num_set:  # this is a sequence start
            length = 1
            current = num
            while current + 1 in num_set:
                current += 1
                length += 1
            best = max(best, length)
    return best
