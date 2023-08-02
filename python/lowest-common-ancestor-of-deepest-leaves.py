# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_lca_depest_leaves(node: Optional[TreeNode], level: int) -> (Optional[TreeNode], int):
        if node == None:
            return node, level
        node_left, depth_left = Solution.get_lca_depest_leaves(node.left, level + 1)
        node_right, depth_right = Solution.get_lca_depest_leaves(node.right, level + 1)
        level = max(depth_left, depth_right)
        if depth_right < depth_left:
            node = node_left
        if depth_left < depth_right:
            node = node_right
        return node, level

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return Solution.get_lca_depest_leaves(root, 0)[0]
