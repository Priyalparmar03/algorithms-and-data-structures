"""Permutations — backtracking with a used-elements tracker."""
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    result = []
    used = [False] * len(nums)

    def backtrack(current: List[int]) -> None:
        if len(current) == len(nums):
            result.append(current.copy())
            return
        for i, num in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            current.append(num)
            backtrack(current)
            current.pop()
            used[i] = False

    backtrack([])
    return result
