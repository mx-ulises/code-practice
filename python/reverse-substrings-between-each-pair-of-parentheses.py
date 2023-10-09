class Solution:
    def reverseParentheses(self, s: str) -> str:
        string_builder = []
        for c in s:
            if c == ")":
                aux_builder = []
                while string_builder[-1] != "(":
                    aux_builder.append(string_builder.pop())
                string_builder.pop()
                string_builder.extend(aux_builder)
            else:
                string_builder.append(c)
        return "".join(string_builder)
