class Solution:

    def arrangeWords(self, text: str) -> str:
        words_array = text.lower().split()
        words = []
        for i in range(len(words_array)):
            word = words_array[i]
            words.append((len(word), i, word))
        words.sort()
        word = list(words[0][2])
        word[0] = word[0].upper()
        words[0] = (len(word), 0, "".join(word))
        return " ".join([word[2] for word in words])
