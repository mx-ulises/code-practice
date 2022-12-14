class Solution:
    def secondHighest(self, s: str) -> int:
        digits = {int(c) for c in s if "0" <= c and c <= "9"}
        if 1 < len(digits):
            digits = list(digits)
            digits.sort()
            return digits[-2]
        return -1
