from solution import TreeNode, level_order


def test_standard_case():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order(root) == [[3], [9, 20], [15, 7]]


def test_empty_tree():
    assert level_order(None) == []


def test_single_node():
    assert level_order(TreeNode(1)) == [[1]]
