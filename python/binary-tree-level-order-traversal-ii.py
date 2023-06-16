# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        s = [(root, 0)]
        while s:
            node, level = s.pop()
            if node == None:
                continue
            if level == len(levels):
                levels.append([])
            levels[level].append(node.val)
            s.append((node.right, level + 1))
            s.append((node.left, level + 1))
        levels.reverse()
        return levels
