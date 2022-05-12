class Solution:
    def isValid(self, s: str) -> bool:
        while s:
            new_s = s.replace("abc", "")
            if new_s == s:
                return False
            s = new_s
        return True

    def isValid2(self, s: str) -> bool:
        stack = []
        for c in s:
            stack.append(c)
            if c == "c":
                if len(stack) < 3:
                    return False
                if stack[-2] == "b" and stack[-3] == "a":
                    stack.pop()
                    stack.pop()
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
