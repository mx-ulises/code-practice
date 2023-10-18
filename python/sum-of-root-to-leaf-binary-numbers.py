# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        total = 0
        s = [(root, 0)]
        while s:
            node, preffix = s.pop()
            new_preffix = (preffix << 1) + node.val
            if node.left == None and node.right == None:
                total += new_preffix
            if node.left != None:
                s.append((node.left, new_preffix))
            if node.right != None:
                s.append((node.right, new_preffix))
        return total
