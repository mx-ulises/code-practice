# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_increasing_bst(node: TreeNode) -> (TreeNode, TreeNode):
        if node == None:
            return None, None
        head_left, tail_left = Solution.get_increasing_bst(node.left)
        head_right, tail_right = Solution.get_increasing_bst(node.right)
        node.left = None
        if tail_left != None:
            tail_left.right = node
        node.right = head_right
        head, tail = head_left, tail_right
        if head == None:
            head = node
        if tail == None:
            tail = node
        return (head, tail)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        return Solution.get_increasing_bst(root)[0]
