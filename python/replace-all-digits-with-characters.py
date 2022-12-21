class Solution:
    def shift(c: str, i: int) -> int:
        return chr(ord(c) + i)

    def replaceDigits(self, s: str) -> str:
        t = []
        for i in range(len(s)):
            if i % 2 == 0:
                t.append(s[i])
            else:
                t.append(Solution.shift(s[i - 1], int(s[i])))
        return ''.join(t)
