# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_deepest_subtree(node: TreeNode, level: int) -> (TreeNode, int):
        if node == None:
            return node, level
        new_level = level + 1
        left_node, left_level = Solution.get_deepest_subtree(node.left, new_level)
        right_node, right_level = Solution.get_deepest_subtree(node.right, new_level)
        if left_level < right_level:
            return right_node, right_level
        if right_level < left_level:
            return left_node, left_level
        return node, left_level

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return Solution.get_deepest_subtree(root, 0)[0]
