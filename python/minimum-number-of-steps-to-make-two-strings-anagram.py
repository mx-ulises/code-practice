class Solution:
    def minSteps(self, s: str, t: str) -> int:
        offset = ord('a')
        char_count = [0] * 26
        min_steps = 0
        for i in range(len(s)):
            s_j = ord(s[i]) - offset
            char_count[s_j] += 1
            t_j = ord(t[i]) - offset
            char_count[t_j] -= 1
        for c in char_count:
            if 0 < c:
                min_steps += c
        return min_steps
