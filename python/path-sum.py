# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def is_leave(node: Optional[TreeNode]) -> bool:
        if node.left == None and node.right == None:
            return True
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        s = [(root, targetSum)]
        while s:
            node, target_sum = s.pop()
            if node == None:
                continue
            if Solution.is_leave(node) and target_sum == node.val:
                return True
            new_target_sum = target_sum - node.val
            s.append((node.left, new_target_sum))
            s.append((node.right, new_target_sum))
        return False
