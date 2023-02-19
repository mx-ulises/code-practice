class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_count = defaultdict(lambda: 0)
        for word in words:
            for c in word:
                char_count[c] += 1
        for c in char_count:
            if char_count[c] % len(words):
                return False
        return True
