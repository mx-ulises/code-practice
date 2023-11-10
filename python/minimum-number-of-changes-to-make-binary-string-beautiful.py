class Solution:
    def minChanges(self, s: str) -> int:
        i = 0
        changes = 0
        while i < len(s):
            if s[i] != s[i + 1]:
                changes += 1
            i += 2
        return changes
