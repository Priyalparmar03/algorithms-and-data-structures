from solution import TreeNode, is_symmetric


def test_symmetric_tree():
    root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
    assert is_symmetric(root) is True


def test_asymmetric_tree():
    root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    assert is_symmetric(root) is False


def test_empty_tree():
    assert is_symmetric(None) is True
