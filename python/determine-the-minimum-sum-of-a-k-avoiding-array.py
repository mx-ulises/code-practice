class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        output = 0
        current = 0
        for current in range(1, min(n + 1, k // 2 + 1)):
            output += current
        for current in range(k, k + n - current):
            output += current
        return output
