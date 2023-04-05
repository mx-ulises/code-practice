class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        # for n = 4, n in base_2 is 100 (non palindromic)
        # for n > 4, n in base_(n - 2) is always 12
        return False
