class Solution:
    def encode_word(word: str) -> int:
        word_encoded = 0
        offset = ord('a')
        for c in word:
            bit_offset = ord(c) - offset
            word_encoded |= (1 << bit_offset)
        return word_encoded

    def maxProduct(self, words: List[str]) -> int:
        encoded_maximum_len = defaultdict(lambda: 0)
        while words:
            word = words.pop()
            word_encoded = Solution.encode_word(word)
            current_max_len = encoded_maximum_len[word_encoded]
            encoded_maximum_len[word_encoded] = max(current_max_len, len(word))
        maximal = 0
        for word_1 in encoded_maximum_len:
            for word_2 in encoded_maximum_len:
                if (word_1 & word_2) == 0:
                    candidate = encoded_maximum_len[word_1] * encoded_maximum_len[word_2]
                    maximal = max(maximal, candidate)
        return maximal

