# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def add_node(node: Optional[TreeNode], output: list):
        if node:
            output.append("(")
            Solution.tree_to_string(node, output)
            output.append(")")

    def tree_to_string(node: Optional[TreeNode], output: list):
        output.append(str(node.val))
        Solution.add_node(node.left, output)
        if node.left == None and node.right:
            output.append("()")
        Solution.add_node(node.right, output)

    def tree2str(self, root: Optional[TreeNode]) -> str:
        output = []
        Solution.tree_to_string(root, output)
        return "".join(output)
