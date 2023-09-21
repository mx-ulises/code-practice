# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def prune_zero_tree(node: Optional[TreeNode]) -> Optional[TreeNode]:
        if node == None:
            return None
        node.left = Solution.prune_zero_tree(node.left)
        node.right = Solution.prune_zero_tree(node.right)
        if node.val == 1 or node.left or node.right:
            return node
        return None

    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return Solution.prune_zero_tree(root)
