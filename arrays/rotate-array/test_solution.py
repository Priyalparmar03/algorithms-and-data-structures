from solution import rotate


def test_standard_case():
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]


def test_k_equals_length():
    nums = [1, 2, 3]
    rotate(nums, 3)
    assert nums == [1, 2, 3]


def test_k_greater_than_length():
    nums = [1, 2, 3]
    rotate(nums, 4)
    assert nums == [3, 1, 2]
