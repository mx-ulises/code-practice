class Solution:
    def is_bad_substring(a: str, b: str) -> bool:
        diff = ord(a) - ord(b)
        return diff == 32 or diff == -32

    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if 0 < len(stack) and Solution.is_bad_substring(stack[-1], c):
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)
