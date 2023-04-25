# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def average_nodes(node: Optional[TreeNode]) -> (int, int, int):
        if node == None:
            return 0, 0, 0
        total_sum = node.val
        total_count = 1
        compliant_count = 0
        left_total_sum, left_total_count, left_compliant_count = Solution.average_nodes(node.left)
        right_total_sum, right_total_count, right_compliant_count = Solution.average_nodes(node.right)
        total_sum += left_total_sum + right_total_sum
        total_count += left_total_count + right_total_count
        compliant_count += left_compliant_count + right_compliant_count
        if (total_sum // total_count) == node.val:
            compliant_count += 1
        return (total_sum, total_count, compliant_count)


    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return Solution.average_nodes(root)[2]
