class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num = 0
        j = 1
        for i in range(1, n + 1):
            if j == m:
                num -= i
                j = 1
            else:
                num += i
                j += 1
        return num
