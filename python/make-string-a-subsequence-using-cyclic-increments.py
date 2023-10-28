class Solution:
    def matches(c1: str, c2: str) -> bool:
        a = ord(c1) - 97
        b = ord(c2) - 97
        return a == b or ((a + 1) % 26) == b

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        pending_1 = len(str1)
        pending_2 = len(str2)
        j = 0
        for i in range(len(str1)):
            if pending_1 < pending_2:
                return False
            if Solution.matches(str1[i], str2[j]):
                j += 1
                pending_2 -= 1
            if j == len(str2):
                return True
            pending_1 -= 1
        return False
