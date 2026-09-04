"""Tower of Hanoi — classic recursive decomposition."""
from typing import List, Tuple


def tower_of_hanoi(n: int, source: str = "A", auxiliary: str = "B", target: str = "C") -> List[Tuple[str, str]]:
    moves = []

    def solve(k: int, src: str, aux: str, tgt: str) -> None:
        if k == 0:
            return
        solve(k - 1, src, tgt, aux)
        moves.append((src, tgt))
        solve(k - 1, aux, src, tgt)

    solve(n, source, auxiliary, target)
    return moves
