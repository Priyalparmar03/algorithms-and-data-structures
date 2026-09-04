from solution import TreeNode, max_depth


def test_balanced_tree():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(root) == 3


def test_empty_tree():
    assert max_depth(None) == 0


def test_single_node():
    assert max_depth(TreeNode(1)) == 1


def test_skewed_tree():
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert max_depth(root) == 3
