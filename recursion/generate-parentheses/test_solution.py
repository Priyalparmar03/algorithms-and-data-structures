from solution import generate_parenthesis


def test_n_equals_3():
    result = set(generate_parenthesis(3))
    expected = {"((()))", "(()())", "(())()", "()(())", "()()()"}
    assert result == expected


def test_n_equals_1():
    assert generate_parenthesis(1) == ["()"]


def test_all_results_are_balanced():
    for s in generate_parenthesis(4):
        balance = 0
        for ch in s:
            balance += 1 if ch == "(" else -1
            assert balance >= 0
        assert balance == 0
