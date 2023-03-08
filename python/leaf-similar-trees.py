# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_leaves(node: Optional[TreeNode], leaves: List[int]):
        if node == None:
            return
        if node.left or node.right:
            Solution.get_leaves(node.left, leaves)
            Solution.get_leaves(node.right, leaves)
        else:
            leaves.append(node.val)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves_1, leaves_2 = [], []
        Solution.get_leaves(root1, leaves_1)
        Solution.get_leaves(root2, leaves_2)
        return leaves_1 == leaves_2
