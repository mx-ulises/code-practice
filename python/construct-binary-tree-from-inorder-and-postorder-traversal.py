# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def build_tree(inorder: List[int], postorder: List[int], start: int, end: int) -> Optional[TreeNode]:
        if end <= start:
            return None
        node = TreeNode(val=postorder.pop())
        i = inorder.index(node.val, start, end + 1)
        node.right = Solution.build_tree(inorder, postorder, i + 1, end)
        node.left = Solution.build_tree(inorder, postorder, start, i)
        return node

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return Solution.build_tree(inorder, postorder, 0, len(inorder))
