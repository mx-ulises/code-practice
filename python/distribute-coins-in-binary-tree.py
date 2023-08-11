# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_required_moves(node: Optional[TreeNode], current_moves: int) -> (int, int):
        if node == None:
            return (0, current_moves)
        left_balance, current_moves = Solution.get_required_moves(node.left, current_moves)
        right_balance, current_moves = Solution.get_required_moves(node.right, current_moves)
        balance = left_balance + right_balance + node.val - 1
        current_moves += abs(left_balance) + abs(right_balance)
        return balance, current_moves

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        return Solution.get_required_moves(root, 0)[1]
