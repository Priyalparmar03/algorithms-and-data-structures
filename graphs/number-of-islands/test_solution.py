from solution import num_islands


def test_standard_case():
    grid = [
        list("11110"),
        list("11010"),
        list("11000"),
        list("00000"),
    ]
    assert num_islands(grid) == 1


def test_multiple_islands():
    grid = [
        list("11000"),
        list("11000"),
        list("00100"),
        list("00011"),
    ]
    assert num_islands(grid) == 3


def test_no_land():
    grid = [list("0000")]
    assert num_islands(grid) == 0
