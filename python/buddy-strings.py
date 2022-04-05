class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append((s[i], goal[i]))
        if len(diff) == 0:
            return len(set(list(s))) < len(s)
        if len(diff) == 2:
            return diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]
        return False
