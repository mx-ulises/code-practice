# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def construct_tree(node: Optional[TreeNode], val: int):
        if node.right == None:
            node.right = TreeNode(val)
        elif node.right.val < val:
            new_node = TreeNode(val)
            new_node.left = node.right
            node.right = new_node
        else:
            Solution.construct_tree(node.right, val)


    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)
        if root.val < val:
            node = TreeNode(val)
            node.left = root
            return node
        Solution.construct_tree(root, val)
        return root
