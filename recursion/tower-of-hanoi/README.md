# Tower Of Hanoi

**Source:** Classic
**Topic:** Recursion
**Difficulty:** Medium

## Problem
Move n disks from a source peg to a target peg (using an auxiliary peg), moving one disk at a time and never placing a larger disk on a smaller one. Return the sequence of moves.

## Approach
The classic recursive decomposition: to move n disks from source to target, first move the top n-1 disks from source to auxiliary (using target as the temporary spare), then move the single largest disk from source to target directly, then move the n-1 disks from auxiliary to target (using source as the spare). Each recursive call reduces the problem by exactly one disk.

## Complexity
- Time: O(2^n) — the minimum number of moves required is provably 2^n - 1, and the algorithm achieves that exactly.
- Space: O(n) — recursion stack depth (plus O(2^n) if all moves are stored in the output).

## Implementation
See `solution.py`.

## Tests
See `test_solution.py`.
