class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        d = 0
        while z:
            d += z % 2
            z = z >> 1
        return d
