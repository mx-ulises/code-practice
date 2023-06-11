# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def create_forest(node: Optional[TreeNode], to_delete_set: Set[int], forest: List[TreeNode]) -> bool:
        if node == None:
            return False
        if Solution.create_forest(node.left, to_delete_set, forest):
            node.left = None
        if Solution.create_forest(node.right, to_delete_set, forest):
            node.right = None
        if node.val in to_delete_set:
            if node.left != None:
                forest.append(node.left)
            if node.right != None:
                forest.append(node.right)
            return True
        return False

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = {item for item in to_delete}
        forest = []
        delete_root = Solution.create_forest(root, to_delete_set, forest)
        if delete_root == False:
            forest.append(root)
        return forest
