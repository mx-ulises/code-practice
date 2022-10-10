# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        s = [(root.left, root.right)]
        while s:
            left, right = s.pop()
            if left == None and right == None:
                continue
            if right == None or left == None:
                return False
            if left.val != right.val:
                return False
            s.append((left.left, right.right))
            s.append((left.right, right.left))
        return True
