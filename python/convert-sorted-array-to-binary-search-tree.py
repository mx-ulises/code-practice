# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        start, end = 0, len(nums) - 1
        mid = (end + start) // 2
        root = TreeNode(val=nums[mid])
        s = [(start, mid - 1, root), (mid + 1, end, root)]
        while s:
            start, end, parent = s.pop()
            if end < start or start < 0 or len(nums) <= end:
                continue
            mid = (end + start) // 2
            node = TreeNode(val=nums[mid])
            if node.val <= parent.val:
                parent.left = node
            else:
                parent.right = node
            s.append((start, mid - 1, node))
            s.append((mid + 1, end, node))
        return root
