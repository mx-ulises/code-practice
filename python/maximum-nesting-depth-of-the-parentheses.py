class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth = 0
        maximal_depth = 0
        for c in s:
            if c == "(":
                current_depth += 1
            elif c == ")":
                maximal_depth = max(maximal_depth, current_depth)
                current_depth -= 1
        return maximal_depth
