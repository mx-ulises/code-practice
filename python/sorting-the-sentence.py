class Solution:
    def sortSentence(self, s: str) -> str:
        indexed_words_pairs = [(int(w[-1]), w[:len(w) - 1]) for w in s.split()]
        indexed_words_pairs.sort()
        return " ".join([pair[1] for pair in indexed_words_pairs])
