# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getSuccessor(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        succesor = None
        current = root
        while current:
            if target < current.val:
                succesor = current
                current = current.left
            else:
                current = current.right
        return succesor
