from solution import is_anagram


def test_valid_anagram():
    assert is_anagram("anagram", "nagaram") is True


def test_not_anagram_different_letters():
    assert is_anagram("rat", "car") is False


def test_different_lengths():
    assert is_anagram("ab", "a") is False


def test_empty_strings():
    assert is_anagram("", "") is True
