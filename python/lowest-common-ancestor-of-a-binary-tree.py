# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def get_lower_common_ancestor(node, p, q):
    """ Base case, Node == Null"""
    if node == None:
        return None, False, False

    """ Left child """
    left_parent, left_found_p, left_found_q = get_lower_common_ancestor(node.left, p, q)
    if left_parent:
        return left_parent, left_found_p, left_found_q

    """ Right child """
    right_parent, right_found_p, right_found_q = get_lower_common_ancestor(node.right, p, q)
    if right_parent:
        return right_parent, right_found_p, right_found_q

    """ Check current level """
    found_p = (p == node) | left_found_p | right_found_p
    found_q = (q == node) | left_found_q | right_found_q
    parent = None
    if found_p and found_q:
        parent = node
    return parent, found_p, found_q


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return get_lower_common_ancestor(root, p, q)[0]
