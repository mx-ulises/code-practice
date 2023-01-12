class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        prev, current = 0, 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current += 1
            else:
                count += min(prev, current)
                prev, current = current, 1
        count += min(prev, current)
        return count
