class Solution:

    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        char_count_original = defaultdict(lambda: 0)
        words.sort(key=len)
        for c in licensePlate.lower():
            if 'a' <= c and c <= 'z':
                char_count_original[c] += 1
        for word in words:
            char_count = char_count_original.copy()
            is_valid_word = True
            for c in word.lower():
                if c in char_count:
                    char_count[c] -= 1
            for c in char_count:
                if 0 < char_count[c]:
                    is_valid_word = False
                    break
            if is_valid_word:
                return word
        return None
