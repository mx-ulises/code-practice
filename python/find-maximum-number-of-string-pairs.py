class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        previous = set()
        for word in words:
            reversed_word = word[::-1]
            if reversed_word in previous:
                previous.remove(reversed_word)
                count += 1
            else:
                previous.add(word)
        return count
