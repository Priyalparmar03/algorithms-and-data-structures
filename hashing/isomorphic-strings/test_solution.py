from solution import is_isomorphic


def test_isomorphic():
    assert is_isomorphic("egg", "add") is True


def test_not_isomorphic():
    assert is_isomorphic("foo", "bar") is False


def test_bijection_violation_many_to_one():
    # 'a' and 'b' both mapping to 'a' violates the one-to-one requirement
    assert is_isomorphic("ab", "aa") is False


def test_different_lengths():
    assert is_isomorphic("ab", "a") is False
