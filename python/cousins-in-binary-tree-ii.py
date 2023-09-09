# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_level_sum(node: Optional[TreeNode], level_sum: Dict[int, int], current_level: int):
        if node == None:
            return
        level_sum[current_level] += node.val
        Solution.get_level_sum(node.left, level_sum, current_level + 1)
        Solution.get_level_sum(node.right, level_sum, current_level + 1)

    def adjust_nodes(node: Optional[TreeNode], level_sum: Dict[int, int], current_level: int, sibling_value: int):
        if node == None:
            return
        node.val = level_sum[current_level] - sibling_value
        sibling_value = 0
        if node.left != None:
            sibling_value += node.left.val
        if node.right != None:
            sibling_value += node.right.val
        Solution.adjust_nodes(node.left, level_sum, current_level + 1, sibling_value)
        Solution.adjust_nodes(node.right, level_sum, current_level + 1, sibling_value)

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sum = defaultdict(lambda: 0)
        Solution.get_level_sum(root, level_sum, 0)
        Solution.adjust_nodes(root, level_sum, 0, root.val)
        return root
