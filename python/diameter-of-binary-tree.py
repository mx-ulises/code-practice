# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def gey_subtree_diameter(node: Optional[TreeNode]) -> (int, int):
        if node == None:
            return (0, 0)
        left_diameter, left_height = Solution.gey_subtree_diameter(node.left)
        right_diameter, right_height = Solution.gey_subtree_diameter(node.right)
        diameter = max(left_diameter, right_diameter, left_height + right_height)
        height = max(left_height, right_height) + 1
        return (diameter, height)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return Solution.gey_subtree_diameter(root)[0]
