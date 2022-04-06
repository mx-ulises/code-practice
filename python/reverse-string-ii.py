class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        output = []
        reversing = True
        stack = []
        for c in s:
            stack.append(c)
            if reversing:
                if len(stack) == k:
                    while stack:
                        output.append(stack.pop())
                    reversing = False
            else:
                output.append(c)
                if len(stack) == k:
                    stack = []
                    reversing = True
        if reversing:
            while stack:
                output.append(stack.pop())
        return "".join(output)
