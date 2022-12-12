# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def get_tilt_and_sum(node: Optional[TreeNode]) -> (int, int):
        if node == None:
            return 0, 0
        left_tilt, left_sum = Solution.get_tilt_and_sum(node.left)
        right_tilt, right_sum = Solution.get_tilt_and_sum(node.right)
        node_tilt =  abs(left_sum - right_sum) + left_tilt + right_tilt
        node_sum = node.val + left_sum + right_sum
        return (node_tilt, node_sum)

    def findTilt(self, root: Optional[TreeNode]) -> int:
        return Solution.get_tilt_and_sum(root)[0]
