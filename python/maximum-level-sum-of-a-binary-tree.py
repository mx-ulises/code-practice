# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = [(root, 1)]
        level_sums = defaultdict(lambda: 0)
        while q:
            node, level = q.pop(0)
            level_sums[level] += node.val
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        maximal_level = 1
        for level in level_sums:
            if level_sums[maximal_level] < level_sums[level]:
                maximal_level = level
        return maximal_level
