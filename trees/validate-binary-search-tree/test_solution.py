from solution import TreeNode, is_valid_bst


def test_valid_bst():
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert is_valid_bst(root) is True


def test_invalid_bst_deep_violation():
    # Right subtree's left child (3) violates the root's value (5) even though
    # it satisfies its immediate parent (6) -- tests the range-propagation, not
    # just parent-child comparison.
    root = TreeNode(5, TreeNode(1), TreeNode(6, TreeNode(3), TreeNode(7)))
    assert is_valid_bst(root) is False


def test_empty_tree():
    assert is_valid_bst(None) is True


def test_single_node():
    assert is_valid_bst(TreeNode(1)) is True
