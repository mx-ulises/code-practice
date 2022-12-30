class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        if n == 0:
            return 0
        summatory = 0
        product = 1
        while n:
            d = n % 10
            n = n // 10
            summatory += d
            product *= d
        return product - summatory
