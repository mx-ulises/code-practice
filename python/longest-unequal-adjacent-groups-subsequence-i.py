class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        output = [words[0]]
        last_group = groups[0]
        for i in range(1, n):
            if groups[i] != last_group:
                output.append(words[i])
                last_group = groups[i]
        return output
