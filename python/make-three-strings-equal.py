class Solution:
    def is_matching_char(strings: List[str], i: int) -> bool:
        c = strings[0][i]
        for s in strings:
            if s[i] != c:
                return False
        return True

    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        strings = [s1, s2, s3]
        if not Solution.is_matching_char(strings, 0):
            return -1
        string_lens = [len(s) for s in strings]
        i = 1
        while i < min(string_lens):
            if not Solution.is_matching_char(strings, i):
                break
            i += 1
        operations = sum(string_lens) - (len(string_lens) * i)
        return operations
