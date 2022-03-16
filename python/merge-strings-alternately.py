class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = []
        i, j = 0, 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                word.append(word1[i])
                i += 1
            if j < len(word2):
                word.append(word2[j])
                j += 1
        return "".join(word)
