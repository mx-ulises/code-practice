class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) - 1
        l = len(s)
        while i < j and s[i] == s[j]:
            c = s[i]
            c_count = 0
            while i < j and c == s[i]:
                i += 1
                c_count += 1
            while i < j and c == s[j]:
                j -= 1
                c_count += 1
            if i == j and c_count and c == s[j]:
                l = 0
            else:
                l = j - i + 1
        return l
