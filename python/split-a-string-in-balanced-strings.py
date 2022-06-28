CHAR_MAP = {"L": 1, "R": -1}

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        current_sum = 0
        for i in range(len(s)):
            current_sum += CHAR_MAP[s[i]]
            if current_sum == 0:
                count += 1
        return count
