class Solution:
    def encode(word, char_mapping):
        encoded_word = []
        for c in word:
            i = ord(c) - ord('a')
            encoded_word.append(char_mapping[i])
        return "".join(encoded_word)

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        char_mapping = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        word_count = set([])
        for word in words:
            word_count.add(Solution.encode(word, char_mapping))
        return len(word_count)
