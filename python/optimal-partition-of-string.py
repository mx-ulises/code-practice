class Solution:
    def solution_map(s: str) -> int:
        current_chars = defaultdict(lambda: 0)
        substrings = 0
        for c in s:
            if current_chars[c] == substrings:
                substrings += 1
            current_chars[c] = substrings
        return substrings


    def solution_array(s: str) -> int:
        current_chars = [0] * 26
        substrings = 0
        for c in s:
            i = ord(c) - ord('a')
            if current_chars[i] == substrings:
                substrings += 1
            current_chars[i] = substrings
        return substrings


    def partitionString(self, s: str) -> int:
        return Solution.solution_map(s)
