"""Combination Sum — backtracking with unlimited reuse and early pruning."""
from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    candidates.sort()  # enables early exit via pruning

    def backtrack(start: int, remaining: int, current: List[int]) -> None:
        if remaining == 0:
            result.append(current.copy())
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break  # sorted candidates -- everything after is too big too
            current.append(candidates[i])
            backtrack(i, remaining - candidates[i], current)  # i, not i+1: allows reuse
            current.pop()

    backtrack(0, target, [])
    return result
