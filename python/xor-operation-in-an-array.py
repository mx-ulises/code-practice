class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        out = 0
        for i in range(n):
            out ^= (start + 2 * i)
        return out
