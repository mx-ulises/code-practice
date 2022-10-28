class Solution:
    def sumBase(self, n: int, k: int) -> int:
        summatory = 0
        while n:
            summatory += n % k
            n = n // k
        return summatory
