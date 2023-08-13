class Solution:
    def minSteps(self, s: str, t: str) -> int:
        char_count = defaultdict(lambda: 0)
        for c in s:
            char_count[c] += 1
        for c in t:
            char_count[c] -= 1
        steps = 0
        for c in char_count:
            steps += abs(char_count[c])
        return steps
