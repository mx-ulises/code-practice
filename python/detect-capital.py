class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        all_capitals = 'A' <= word[0] and word[0] <= 'Z'
        only_first_capital = all_capitals
        all_non_capitals = 'a' <= word[0] and word[0] <= 'z'
        i = 1
        while i < len(word):
            if 'A' <= word[i] and word[i] <= 'Z':
                all_non_capitals = False
                only_first_capital = False
            if 'a' <= word[i] and word[i] <= 'z':
                all_capitals = False
            i += 1
        return all_capitals or all_non_capitals or only_first_capital
