from solution import knapsack


def test_standard_case():
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    assert knapsack(weights, values, 7) == 9  # items with weight 3+4


def test_zero_capacity():
    assert knapsack([1, 2], [10, 20], 0) == 0


def test_all_items_fit():
    assert knapsack([1, 1], [5, 5], 10) == 10


def test_no_items():
    assert knapsack([], [], 5) == 0
