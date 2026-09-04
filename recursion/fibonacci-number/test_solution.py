from solution import fib


def test_base_cases():
    assert fib(0) == 0
    assert fib(1) == 1


def test_standard_case():
    assert fib(10) == 55


def test_larger_value_runs_fast_due_to_memoization():
    assert fib(35) == 9227465
