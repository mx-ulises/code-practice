# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        s = [(root, 0)]
        bottom_left_value = 0
        deeper_level = -1
        while s:
            node, level = s.pop()
            if node == None:
                continue
            if deeper_level < level:
                deeper_level = level
                bottom_left_value = node.val
            next_level = level + 1
            s.append((node.right, next_level))
            s.append((node.left, next_level))
        return bottom_left_value
