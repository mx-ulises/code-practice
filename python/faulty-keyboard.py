class Solution:
    def finalString(self, s: str) -> str:
        string_builder = Deque()
        reverse = False
        for c in s:
            if c == 'i':
                reverse ^= True
            elif reverse:
                string_builder.appendleft(c)
            else:
                string_builder.append(c)
        if reverse:
            string_builder.reverse()
        return "".join(string_builder)
