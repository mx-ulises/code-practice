class Solution:
    def generate(n: int) -> str:
        if n == 0:
            return ""
        suffix = Solution.generate(n // 2) * 2
        if n & 1 == 1:
            return "a" + suffix
        return suffix

    def generateTheString(self, n: int) -> str:
        if n & 1 == 1:
            return Solution.generate(n)
        else:
            return "b" + Solution.generate(n - 1)
