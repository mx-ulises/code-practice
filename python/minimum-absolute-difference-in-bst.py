# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def compute_minimal(self, node):
        most_left, most_right = node, node
        if node.left:
            most_left, right = self.compute_minimal(node.left)
            self.minimal = min(self.minimal, node.val - right.val)
        if node.right:
            left, most_right = self.compute_minimal(node.right)
            self.minimal = min(self.minimal, left.val - node.val)
        return (most_left, most_right)
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minimal = 10000
        self.compute_minimal(root)
        return self.minimal
