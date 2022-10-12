# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_height_if_balanced(node: Optional[TreeNode]) -> int:
        if node == None:
            return 0
        left_height = Solution.get_height_if_balanced(node.left)
        if left_height < 0:
            return -1
        right_height = Solution.get_height_if_balanced(node.right)
        if right_height < 0:
            return -1
        height_diff = abs(left_height - right_height)
        if 1 < height_diff:
            return - 1
        return max(left_height, right_height) + 1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return 0 <= Solution.get_height_if_balanced(root)
