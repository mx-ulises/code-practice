# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_maximum_binary_tree(nums: List[int], start: int, end: int) -> Optional[TreeNode]:
        if end <= start:
            return None
        maximal_i = start
        maximal = 0
        for i in range(start, end):
            if maximal <= nums[i]:
                maximal = nums[i]
                maximal_i = i
        node = TreeNode(maximal)
        node.left = Solution.get_maximum_binary_tree(nums, start, maximal_i)
        node.right = Solution.get_maximum_binary_tree(nums, maximal_i + 1, end)
        return node

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return Solution.get_maximum_binary_tree(nums, 0, len(nums))
