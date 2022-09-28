# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def print_path(node, path_list, current_path):
        if node == None:
            return True
        current_path.append(str(node.val))
        left_is_none = Solution.print_path(node.left, path_list, current_path)
        right_is_none = Solution.print_path(node.right, path_list, current_path)
        if left_is_none and right_is_none:
            path_list.append("->".join(current_path))
        current_path.pop()
        return False


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path_list = []
        current_path = []
        Solution.print_path(root, path_list, current_path)
        return path_list
