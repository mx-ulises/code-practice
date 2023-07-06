class Solution:
    def removeStars(self, s: str) -> str:
        output = []
        for c in s:
            if c == "*":
                output.pop()
            else:
                output.append(c)
        return "".join(output)
