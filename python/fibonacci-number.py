class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        f, g = 0, 1
        for _ in range(1, n):
            x = f + g
            f = g
            g = x
        return g
