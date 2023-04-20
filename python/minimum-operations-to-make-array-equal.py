class Solution:
    def minOperations(self, n: int) -> int:
        summatory = n + ((n - 1) * n)
        avg = summatory // n
        m = n // 2
        summatory_m = m + ((m - 1) * m)
        result = (avg * (n // 2)) - summatory_m
        return result
