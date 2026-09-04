from solution import longest_common_subsequence


def test_standard_case():
    assert longest_common_subsequence("abcde", "ace") == 3


def test_no_common_subsequence():
    assert longest_common_subsequence("abc", "def") == 0


def test_identical_strings():
    assert longest_common_subsequence("abc", "abc") == 3


def test_empty_string():
    assert longest_common_subsequence("", "abc") == 0
