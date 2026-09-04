from solution import TreeNode, right_side_view


def test_standard_case():
    root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    assert right_side_view(root) == [1, 3, 4]


def test_empty_tree():
    assert right_side_view(None) == []


def test_left_only_tree():
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert right_side_view(root) == [1, 2, 3]
