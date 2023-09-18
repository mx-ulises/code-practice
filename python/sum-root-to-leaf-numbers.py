# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s = [(root, 0)]
        summatory = 0
        while s:
            node, prev_sum = s.pop()
            current_sum = 10 * prev_sum + node.val
            is_leaf = True
            if node.left != None:
                s.append((node.left, current_sum))
                is_leaf = False
            if node.right != None:
                s.append((node.right, current_sum))
                is_leaf = False
            if is_leaf:
                summatory += current_sum
        return summatory
