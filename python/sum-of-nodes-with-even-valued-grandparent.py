# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        s = [(root, -1, -1)]
        node_sum = 0
        while s:
            node, parent_value, gp_value = s.pop()
            if node == None:
                continue
            if gp_value & 1 == 0:
                node_sum += node.val
            s.append((node.left, node.val, parent_value))
            s.append((node.right, node.val, parent_value))
        return node_sum
