VOWELS = set(['a', 'e', 'i', 'o', 'u'])

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        for i in range(left, right + 1):
            word = words[i]
            if word[0] in VOWELS and word[-1] in VOWELS:
                count += 1
        return count
