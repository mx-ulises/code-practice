class Solution:
    def isValid(self, s: str) -> bool:
        while s:
            new_s = s.replace("abc", "")
            if new_s == s:
                return False
            s = new_s
        return True
