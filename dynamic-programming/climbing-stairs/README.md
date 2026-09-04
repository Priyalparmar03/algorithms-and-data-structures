# Climbing Stairs

**Source:** LeetCode #70
**Topic:** Dynamic Programming
**Difficulty:** Easy

## Problem
You're climbing n stairs; each step you can climb 1 or 2 stairs. How many distinct ways can you reach the top?

## Approach
The number of ways to reach step n is the sum of ways to reach step n-1 (then take one more step) and step n-2 (then take a two-step) — this is exactly the Fibonacci recurrence. Naive recursion recomputes overlapping subproblems exponentially; bottom-up DP builds up from the base cases iteratively, storing only the last two values since that's all each step depends on.

## Complexity
- Time: O(n) — single pass.
- Space: O(1) — only two running variables needed (space-optimized from an O(n) DP table).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
Recognizing this as 'just Fibonacci with different framing' is the actual insight — worth stating explicitly, since DP problems often turn out to be familiar recurrences wearing a different word problem.
