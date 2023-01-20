class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        sign = 1
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i == len(s):
            return 0
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        while i < len(s) and ord('0') <= ord(s[i]) and ord(s[i]) <= ord('9'):
            num = num * 10 + ord(s[i]) - ord('0')
            i += 1
        if sign == 1:
            return min(2147483648 - 1, num)
        return max(-2147483648, -num)
