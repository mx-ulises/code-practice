# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        s = [(root, 1001)]
        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            while s[-1][1] < node.val:
                s.pop()
            parent, upper_bound = s[-1]
            if node.val < parent.val:
                parent.left = node
                s.append((node, parent.val))
            else:
                parent.right = node
                s.append((node, upper_bound))
        return root
