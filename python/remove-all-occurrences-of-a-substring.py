class Solution:
    def get_prefix_mapper(part: str) -> List[int]:
        prefix_mapper = [0] * len(part)
        j = 0
        for i in range(1, len(part)):
            while j and part[i] != part[j]:
                j = prefix_mapper[j - 1]
            if part[i] == part[j]:
                j += 1
            prefix_mapper[i] = j
        return prefix_mapper

    def removeOccurrences(self, s: str, part: str) -> str:
        prefix_mapper = Solution.get_prefix_mapper(part)
        stack = []
        j = 0
        for c in s:
            if stack:
                j = stack[-1][1]
            while j and c != part[j]:
                j = prefix_mapper[j - 1]
            if c == part[j]:
                j += 1
            stack.append((c, j))
            if j == len(part):
                while j:
                    stack.pop()
                    j -= 1
        return "".join([entry[0] for entry in stack])
