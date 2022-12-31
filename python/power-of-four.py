class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        x = int(math.log(n, 4))
        return (4 ** x) == n
