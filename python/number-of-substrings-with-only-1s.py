class Solution:
    def numSub(self, s: str) -> int:
        count = 0
        current = 0
        for c in s:
            if c == "0":
                current = 0
            if c == "1":
                current += 1
                count += current
        return count % 1000000007
