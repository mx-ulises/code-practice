# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s = [root]
        output = []
        while s:
            node = s.pop()
            if node == None:
                continue
            output.append(node.val)
            s.append(node.right)
            s.append(node.left)
        return output
