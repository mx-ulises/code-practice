# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def evaluate(node: Optional[TreeNode]) -> bool:
        if node.val == 0:
            return False
        if node.val == 1:
            return True
        if node.val == 2:
            return Solution.evaluate(node.left) or Solution.evaluate(node.right)
        return Solution.evaluate(node.left) and Solution.evaluate(node.right)

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return Solution.evaluate(root)
