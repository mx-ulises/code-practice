# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        s = [root]
        count = 0
        while s:
            node = s.pop()
            if node == None:
                continue
            count += 1
            s.append(node.left)
            s.append(node.right)
        return count
