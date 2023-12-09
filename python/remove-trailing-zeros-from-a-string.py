class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = list(num)
        while 1 < len(num) and num[-1] == "0":
            num.pop()
        return "".join(num)
