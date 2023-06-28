# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverse_level(q: List[Optional[TreeNode]], n: int):
        for i in range(n // 2):
            j = n - i - 1
            q[i].val, q[j].val = q[j].val, q[i].val

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = [root]
        level = 0
        while q:
            n = len(q)
            if level & 1 == 1:
                Solution.reverse_level(q, n)
            for _ in range(n):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return root
