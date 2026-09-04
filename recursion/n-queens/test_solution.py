from solution import solve_n_queens


def test_n_equals_4_has_two_solutions():
    result = solve_n_queens(4)
    assert len(result) == 2


def test_n_equals_1():
    assert solve_n_queens(1) == [["Q"]]


def test_n_equals_2_and_3_have_no_solution():
    assert solve_n_queens(2) == []
    assert solve_n_queens(3) == []
