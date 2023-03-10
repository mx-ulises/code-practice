class Solution:
    def is_no_zero(a: int) -> bool:
        while a:
            if a % 10 == 0:
                return False
            a //= 10
        return True

    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1, n):
            b = n - a
            if Solution.is_no_zero(a) and Solution.is_no_zero(b):
                return [a, b]
        return None
