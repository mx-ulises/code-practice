# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insert(node: Optional[TreeNode], val: int):
        if val < node.val:
            if node.left == None:
                node.left = TreeNode(val=val)
            else:
                Solution.insert(node.left, val)
        else:
            if node.right == None:
                node.right = TreeNode(val=val)
            else:
                Solution.insert(node.right, val)


    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            root = TreeNode(val=val)
        else:
            Solution.insert(root, val)
        return root
