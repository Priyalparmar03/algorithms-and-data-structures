from solution import merge

def test_standard_case():
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]

def test_touching_intervals():
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]

def test_no_overlap():
    assert merge([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]

def test_single_interval():
    assert merge([[1, 4]]) == [[1, 4]]
