# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        level_start = defaultdict(lambda: None)
        level_end = defaultdict(lambda: None)
        q = [(root, 1, 1)]
        while q:
            node, level, num = q.pop(0)
            if node:
                if not level_start[level]:
                    level_start[level] = num
                level_end[level] = num
                q.append((node.left, level + 1, num * 2))
                q.append((node.right, level + 1, num * 2 + 1))
        maximal = 1
        for level in level_start:
            maximal = max(maximal, level_end[level] - level_start[level] + 1)
        return maximal
