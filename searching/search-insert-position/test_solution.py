from solution import search_insert


def test_target_found():
    assert search_insert([1, 3, 5, 6], 5) == 2


def test_insert_in_middle():
    assert search_insert([1, 3, 5, 6], 2) == 1


def test_insert_at_end():
    assert search_insert([1, 3, 5, 6], 7) == 4


def test_insert_at_start():
    assert search_insert([1, 3, 5, 6], 0) == 0


def test_empty_array():
    assert search_insert([], 5) == 0
