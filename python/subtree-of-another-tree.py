# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check_subtree_common_root(root: Optional[TreeNode], sub_tree: Optional[TreeNode]) -> bool:
        if root == None and sub_tree == None:
            return True
        elif root == None or sub_tree == None:
            return False
        elif root.val == sub_tree.val:
            return Solution.check_subtree_common_root(root.left, sub_tree.left) and Solution.check_subtree_common_root(root.right, sub_tree.right)
        return False

    def check_subtree(root: Optional[TreeNode], sub_tree: Optional[TreeNode]) -> bool:
        if root == None and sub_tree == None:
            return True
        elif root == None or sub_tree == None:
            return False
        elif Solution.check_subtree_common_root(root, sub_tree):
            return True
        else:
            return Solution.check_subtree(root.left, sub_tree) or Solution.check_subtree(root.right, sub_tree)

    def isSubtree(self, root: Optional[TreeNode], sub_tree: Optional[TreeNode]) -> bool:
        return Solution.check_subtree(root, sub_tree)
