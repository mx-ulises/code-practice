class Solution:
    def reformat(self, s: str) -> str:
        alpha = []
        numeric = []
        for c in s:
            if "0" <= c <= "9":
                numeric.append(c)
            if "a" <= c <= "z":
                alpha.append(c)
        maximal, minimal = alpha, numeric
        if len(alpha) < len(numeric):
            maximal, minimal = numeric, alpha
        output = []
        if 1 < len(maximal) - len(minimal):
            return ""
        while maximal:
            output.append(maximal.pop())
            if minimal:
                output.append(minimal.pop())
        return "".join(output)
