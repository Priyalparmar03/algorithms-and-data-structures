from solution import sort_colors


def test_standard_case():
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]


def test_already_sorted():
    nums = [0, 1, 2]
    sort_colors(nums)
    assert nums == [0, 1, 2]


def test_all_same_value():
    nums = [1, 1, 1]
    sort_colors(nums)
    assert nums == [1, 1, 1]


def test_reverse_order():
    nums = [2, 1, 0]
    sort_colors(nums)
    assert nums == [0, 1, 2]
