class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = defaultdict(lambda: 0)
        for c in s:
            char_count[c] += 1
        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i
        return -1
