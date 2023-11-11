# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()
        s = [root]
        while s:
            node = s.pop()
            if node == None:
                continue
            if (k - node.val) in visited:
                return True
            visited.add(node.val)
            s.append(node.left)
            s.append(node.right)
        return False
