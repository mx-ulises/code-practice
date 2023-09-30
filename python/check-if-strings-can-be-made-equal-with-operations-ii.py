OFFSET = ord('a')

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even_index_count = [0] * 26
        odd_index_count = [0] * 26
        index_groups = [even_index_count, odd_index_count]
        for i in range(len(s1)):
            group = i & 1
            a = ord(s1[i]) - OFFSET
            b = ord(s2[i]) - OFFSET
            index_groups[group][a] += 1
            index_groups[group][b] -= 1
        for i in range(26):
            if even_index_count[i] or odd_index_count[i]:
                return False
        return True
