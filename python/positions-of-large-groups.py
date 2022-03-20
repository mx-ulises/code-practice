class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        current = s[0]
        i = 0, j = 0
        output = []
        for j in range(1, len(s)):
            if s[j] != current:
                if 3 <= (j - i):
                    output.append([i, j - 1])
                i = j
            current = s[j]
        j += 1
        if 3 <= (j - i):
            output.append([i, j - 1])
        return output
