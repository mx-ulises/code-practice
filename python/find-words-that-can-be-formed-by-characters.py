class Solution:

    def get_count_char(self, word):
        char_count = defaultdict(lambda: 0)
        for c in word:
            char_count[c] += 1
        return char_count

    def is_good(self, word_char_count, char_count):
        for c in word_char_count:
            if char_count[c] < word_char_count[c]:
                return False
        return True

    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = self.get_count_char(chars)
        word_char_sum = 0
        for word in words:
            if self.is_good(self.get_count_char(word), char_count):
                word_char_sum += len(word)
        return word_char_sum
