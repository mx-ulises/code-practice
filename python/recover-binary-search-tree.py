# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_inorder(node: Optional[TreeNode], inorder: List[Optional[TreeNode]]):
        if node == None:
            return
        Solution.get_inorder(node.left, inorder)
        if 0 == len(inorder):
            inorder.append(node)
        elif len(inorder) == 1:
            if inorder[-1].val < node.val:
                inorder.pop()
            inorder.append(node)
        elif len(inorder) == 2 and node.val < inorder[-1].val:
            inorder.pop()
            inorder.append(node)
        Solution.get_inorder(node.right, inorder)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder = []
        Solution.get_inorder(root, inorder)
        left, right = inorder
        left.val, right.val = right.val, left.val
