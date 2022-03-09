# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def max_ancestor_diff(node, maximal, minimal):
    if node == None:
        return 0
    max_diff = max(abs(node.val - maximal), abs(node.val - minimal))
    maximal = max(node.val, maximal)
    minimal = min(node.val, minimal)
    max_diff = max(max_ancestor_diff(node.left, maximal, minimal), max_diff)
    max_diff = max(max_ancestor_diff(node.right, maximal, minimal), max_diff)
    return max_diff

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max_ancestor_diff(root, root.val, root.val)
