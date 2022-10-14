class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map_s = {}
        char_map_t = {}
        for i in range(len(s)):
            c, d = s[i], t[i]
            if c not in char_map_s:
                char_map_s[c] = d
            if d not in char_map_t:
                char_map_t[d] = c
            if char_map_s[c] != d or char_map_t[d] != c:
                return False
        return True
