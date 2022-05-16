class Solution:
    def maxScore(self, s: str) -> int:
        right = 0
        left = 0
        maximal = 0
        for c in s:
            if c == '1':
                right += 1
        for i in range(len(s) - 1):
            if s[i] == '0':
                left += 1
            else:
                right -= 1
            maximal = max(maximal, left + right)
        return maximal
