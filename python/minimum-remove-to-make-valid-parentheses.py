class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove_index_stack = []
        n = len(s)
        for i in range(n):
            c = s[i]
            if c == "(":
                remove_index_stack.append((c, i))
            if c == ")":
                if not remove_index_stack or remove_index_stack[-1][0] == ")":
                    remove_index_stack.append((c, i))
                else:
                    remove_index_stack.pop()
        remove_index_set = set([i for (_, i) in remove_index_stack])
        output_array = []
        for i in range(n):
            if i in remove_index_set:
                continue
            output_array.append(s[i])
        return "".join(output_array)
