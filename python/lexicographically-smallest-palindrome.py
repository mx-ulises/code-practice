class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        n = len(s)
        for i in range(n // 2):
            j = n - i - 1
            if s[i] != s[j]:
                minimal = chr(min(ord(s[i]), ord(s[j])))
                s[i] = minimal
                s[j] = minimal
        return "".join(s)
