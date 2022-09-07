class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_count = defaultdict(lambda: 0)
        for c in s:
            char_count[c] += 1
        for c in t:
            if not char_count.get(c, 0):
                return c
            char_count[c] -= 1
        return "0"
