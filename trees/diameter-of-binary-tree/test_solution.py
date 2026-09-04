from solution import TreeNode, diameter_of_binary_tree


def test_standard_case():
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert diameter_of_binary_tree(root) == 3


def test_single_node():
    assert diameter_of_binary_tree(TreeNode(1)) == 0


def test_empty_tree():
    assert diameter_of_binary_tree(None) == 0


def test_diameter_can_pass_through_root():
    # Longest path (6-4-2-1-3, 4 edges) passes through the root, longer than
    # the 3-edge path entirely within the left subtree (6-4-2-5).
    left = TreeNode(2, TreeNode(4, TreeNode(6), None), TreeNode(5))
    root = TreeNode(1, left, TreeNode(3))
    assert diameter_of_binary_tree(root) == 4
