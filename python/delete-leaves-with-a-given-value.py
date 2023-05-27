# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delete_leaves(node: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if node == None:
            return None
        node.left = Solution.delete_leaves(node.left, target)
        node.right = Solution.delete_leaves(node.right, target)
        if node.left == None and node.right == None and node.val == target:
            return None
        return node

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        return Solution.delete_leaves(root, target)
