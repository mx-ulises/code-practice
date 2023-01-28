# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def merge_sub_tree(node_1: Optional[TreeNode], node_2: Optional[TreeNode]) -> Optional[TreeNode]:
        if node_1 == None and node_2 == None:
            return None
        if node_1 == None:
            return node_2
        if node_2 == None:
            return node_1
        left = Solution.merge_sub_tree(node_1.left, node_2.left)
        right = Solution.merge_sub_tree(node_1.right, node_2.right)
        return TreeNode(val=node_1.val + node_2.val, left=left, right=right)

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return Solution.merge_sub_tree(root1, root2)
