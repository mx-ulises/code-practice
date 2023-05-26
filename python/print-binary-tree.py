# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_nodes_in_levels(
        node: Optional[TreeNode],
        nodes_in_levels: List[List[List[int]]],
        level: int = 0,
        position: int = 0
        ):
        if node:
            if level == len(nodes_in_levels):
                nodes_in_levels.append([])
            nodes_in_levels[level].append((node.val, position))
            new_position = position << 1
            level += 1
            Solution.get_nodes_in_levels(node.left, nodes_in_levels, level, new_position)
            Solution.get_nodes_in_levels(node.right, nodes_in_levels, level, new_position + 1)

    def get_solution(nodes_in_levels: List[List[List[int]]]) -> List[List[str]]:
        solution = []
        levels = len(nodes_in_levels)
        level_width = (2 ** levels) - 1
        margin = 0
        while nodes_in_levels:
            solution.append([""] * level_width)
            nodes_in_level = nodes_in_levels.pop()
            while nodes_in_level:
                node, position = nodes_in_level.pop()
                real_position = position * margin * 2 + position * 2 + margin
                solution[-1][real_position] = str(node)
            margin = margin * 2 + 1
        solution.reverse()
        return solution

    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        nodes_in_levels = []
        Solution.get_nodes_in_levels(root, nodes_in_levels)
        solution = Solution.get_solution(nodes_in_levels)
        return solution
