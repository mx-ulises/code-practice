# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        s = deque()
        s.append((root, 1))
        while s:
            node, depth = s.popleft()
            if node.right == None and node.left == None:
                return depth
            if node.right != None:
                s.append((node.right, depth + 1))
            if node.left != None:
                s.append((node.left, depth + 1))
