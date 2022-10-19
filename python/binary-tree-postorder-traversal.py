# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def post_order_traversal(node, l):
        if node != None:
            Solution.post_order_traversal(node.left, l)
            Solution.post_order_traversal(node.right, l)
            l.append(node.val)
        return l


    def post_order_traversal_iterative(node):
        l = []
        s = [node]
        while s:
            node = s.pop()
            if node != None:
                s.append(node.left)
                s.append(node.right)
                l.append(node.val)
        l.reverse()
        return l


    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        return Solution.post_order_traversal_iterative(root)
