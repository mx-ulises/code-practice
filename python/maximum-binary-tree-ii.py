# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def construct_tree(node: Optional[TreeNode], new_node: Optional[TreeNode]):
        if node.right == None:
            node.right = new_node
        elif node.right.val < new_node.val:
            new_node.left = node.right
            node.right = new_node
        else:
            Solution.construct_tree(node.right, new_node)


    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if root == None:
            return new_node
        if root.val < val:
            new_node.left = root
            return new_node
        Solution.construct_tree(root, new_node)
        return root
