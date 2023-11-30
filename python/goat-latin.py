VOWELS = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

class Solution:
    def translate_word(word: str, i: int) -> str:
        if word[0] not in VOWELS:
            word = word[1:] + word[0]
        ma = 'm' + ('a' * i)
        return word + ma

    def toGoatLatin(self, sentence: str) -> str:
        string_builder = []
        i = 1
        for word in sentence.split():
            i += 1
            string_builder.append(Solution.translate_word(word, i))
        return " ".join(string_builder)
