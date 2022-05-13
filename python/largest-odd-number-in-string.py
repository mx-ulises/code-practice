class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in range(n):
            j = n - i - 1
            if int(num[j]) % 2:
                return num[:j + 1]
        return ""
