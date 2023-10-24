# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        s = [(root, 0)]
        output = []
        while s:
            node, level = s.pop()
            if node == None:
                continue
            if len(output) == level:
                output.append(node.val)
            output[level] = max(output[level], node.val)
            s.append((node.left, level + 1))
            s.append((node.right, level + 1))
        return output
