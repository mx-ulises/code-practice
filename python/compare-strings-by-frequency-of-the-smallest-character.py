def get_flsc(word):
    smaller_char = 'z'
    char_count = 0
    for c in word:
        if c < smaller_char:
            smaller_char = c
            char_count = 0
        if c == smaller_char:
            char_count += 1
    return char_count


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        words_flsc = []
        for word in words:
            words_flsc.append(get_flsc(word))
        words_flsc.sort()
        frequencies = []
        for query in queries:
            frequencies.append(len(words) - bisect_right(words_flsc, get_flsc(query)))
        return frequencies
