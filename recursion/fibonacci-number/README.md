# Fibonacci Number

**Source:** LeetCode #509
**Topic:** Recursion
**Difficulty:** Easy

## Problem
Compute the nth Fibonacci number.

## Approach
Naive recursion (fib(n) = fib(n-1) + fib(n-2)) recomputes the same subproblems exponentially many times — O(2^n). Adding memoization (a cache of already-computed results) turns it into O(n), since each n is computed exactly once. Included here specifically to demonstrate the recursion-to-memoization transition, before dynamic-programming/ covers the same idea in a fully bottom-up, table-based style.

## Complexity
- Time: O(n) with memoization (O(2^n) naive recursion without it).
- Space: O(n) — memo dictionary plus O(n) recursion stack depth.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.

## Reflection
Without @lru_cache, fib(35) would take several seconds due to exponential blowup — timing this difference is a good concrete demonstration of why memoization matters, not just an abstract complexity claim.
