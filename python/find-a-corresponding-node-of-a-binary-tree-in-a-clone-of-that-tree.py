# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        s = [(original, cloned)]
        while s:
            original, cloned = s.pop()
            if original == None:
                continue
            if original == target:
                return cloned
            s.append((original.left, cloned.left))
            s.append((original.right, cloned.right))
        return None
