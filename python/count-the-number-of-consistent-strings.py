class Solution:
    def is_consistent_word(allowed: Set[int], word: str) -> bool:
        for c in word:
            if c not in allowed:
                return False
        return True

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        consistent = 0
        for word in words:
            if Solution.is_consistent_word(allowed, word):
                consistent += 1
        return consistent
