from solution import top_k_frequent


def test_standard_case():
    assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}


def test_k_equals_length():
    assert set(top_k_frequent([1, 2], 2)) == {1, 2}


def test_single_element():
    assert top_k_frequent([1], 1) == [1]
