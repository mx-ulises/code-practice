class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 1
        current_power = 1
        c = s[0]
        for i in range(1, len(s)):
            if c == s[i]:
                current_power += 1
                max_power = max(max_power, current_power)
            else:
                c = s[i]
                current_power = 1
        return max(max_power, current_power)
