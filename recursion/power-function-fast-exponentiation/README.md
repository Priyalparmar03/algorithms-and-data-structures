# Power Function Fast Exponentiation

**Source:** LeetCode #50 (pow(x, n))
**Topic:** Recursion
**Difficulty:** Medium

## Problem
Implement pow(x, n) — compute x raised to the integer power n, including negative n.

## Approach
Naive repeated multiplication is O(n). Fast exponentiation halves the work at each recursive step using the identity x^n = (x^(n/2))^2 for even n, and x^n = x * (x^(n-1)) for odd n — this is the same divide-and-conquer halving idea as binary search, applied to exponentiation instead of searching. Handle negative n by computing 1 / x^(-n).

## Complexity
- Time: O(log n) — the exponent halves each recursive call.
- Space: O(log n) — recursion stack depth.

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
