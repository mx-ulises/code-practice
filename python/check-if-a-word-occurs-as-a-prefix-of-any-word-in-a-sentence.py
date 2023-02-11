class Solution:
    def is_prefix(word, prefix):
        if len(word) < len(prefix):
            return False
        for i in range(len(prefix)):
            if word[i] != prefix[i]:
                return False
        return True

    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        i = 1
        for word in sentence.split():
            if Solution.is_prefix(word, searchWord):
                return i
            i += 1
        return -1
