class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximal_word_count = 0
        for sentence in sentences:
            word_count = 1 + sentence.count(' ')
            maximal_word_count = max(maximal_word_count, word_count)
        return maximal_word_count
