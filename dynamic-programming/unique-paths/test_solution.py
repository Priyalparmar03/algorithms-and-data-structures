from solution import unique_paths


def test_standard_case():
    assert unique_paths(3, 7) == 28


def test_single_row():
    assert unique_paths(1, 5) == 1


def test_single_column():
    assert unique_paths(5, 1) == 1


def test_square_grid():
    assert unique_paths(3, 3) == 6
