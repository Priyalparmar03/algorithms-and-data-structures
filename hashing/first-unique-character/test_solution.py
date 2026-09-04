from solution import first_uniq_char


def test_standard_case():
    assert first_uniq_char("leetcode") == 0


def test_first_unique_not_at_start():
    assert first_uniq_char("loveleetcode") == 2


def test_no_unique_character():
    assert first_uniq_char("aabb") == -1


def test_empty_string():
    assert first_uniq_char("") == -1
