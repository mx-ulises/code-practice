# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def is_leaf(node: Optional[TreeNode]) -> bool:
        return node.left == None and node.right == None


    def sum_of_left_leaves(node: Optional[TreeNode], is_left_child) -> int:
        if node == None:
            return 0
        elif not Solution.is_leaf(node):
            return Solution.sum_of_left_leaves(node.left, True) + Solution.sum_of_left_leaves(node.right, False)
        elif is_left_child:
            return node.val
        return 0


    def sum_of_left_leaves_iterative(root: Optional[TreeNode]) -> int:
        s = [(root, False)]
        summatory = 0
        while s:
            node, is_left_child = s.pop()
            if node == None:
                continue
            elif not Solution.is_leaf(node):
                s.append((node.left, True))
                s.append((node.right, False))
            elif is_left_child:
                summatory += node.val
        return summatory


    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        #return Solution.sum_of_left_leaves_iterative(root)
        return Solution.sum_of_left_leaves(root, False)
