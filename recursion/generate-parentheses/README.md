# Generate Parentheses

**Source:** LeetCode #22
**Topic:** Recursion
**Difficulty:** Medium

## Problem
Given n pairs of parentheses, generate all combinations of well-formed parentheses strings.

## Approach
Backtracking: build the string one character at a time, at each step choosing to add '(' (allowed whenever fewer than n open parens have been used) or ')' (allowed whenever fewer close parens have been used than opens so far — this is what guarantees well-formedness). Track counts of opens and closes used so far as recursion state instead of re-scanning the partial string each time.

## Complexity
- Time: O(4^n / sqrt(n)) — bounded by the nth Catalan number (the number of valid combinations), a known tight bound for this problem.
- Space: O(n) — recursion depth (excluding output storage).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
