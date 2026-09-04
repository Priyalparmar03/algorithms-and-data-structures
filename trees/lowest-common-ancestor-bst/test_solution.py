from solution import TreeNode, lowest_common_ancestor


def build_bst():
    #         6
    #       /   \
    #      2     8
    #     / \   / \
    #    0   4 7   9
    #       / \
    #      3   5
    n0, n3, n5 = TreeNode(0), TreeNode(3), TreeNode(5)
    n4 = TreeNode(4, n3, n5)
    n2 = TreeNode(2, n0, n4)
    n7, n9 = TreeNode(7), TreeNode(9)
    n8 = TreeNode(8, n7, n9)
    root = TreeNode(6, n2, n8)
    return root, n2, n8, n0, n4


def test_lca_across_subtrees():
    root, n2, n8, _, _ = build_bst()
    assert lowest_common_ancestor(root, n2, n8) is root


def test_lca_ancestor_is_one_of_the_nodes():
    root, n2, _, n0, n4 = build_bst()
    assert lowest_common_ancestor(root, n2, n4) is n2
