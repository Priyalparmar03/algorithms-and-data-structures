from solution import build_list, is_palindrome


def test_palindrome_even():
    assert is_palindrome(build_list([1, 2, 2, 1])) is True


def test_palindrome_odd():
    assert is_palindrome(build_list([1, 2, 3, 2, 1])) is True


def test_not_palindrome():
    assert is_palindrome(build_list([1, 2, 3])) is False


def test_single_node():
    assert is_palindrome(build_list([1])) is True
