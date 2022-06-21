class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_pos = {}
        maximal_distance = -1
        for i in range(len(s)):
            c = s[i]
            if c not in char_pos:
                char_pos[c] = i
            maximal_distance = max(maximal_distance, i - char_pos[c] - 1)
        return maximal_distance
