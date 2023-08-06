class Solution:
    def get_permutation(prefix: List[int], pattern: str, i: int) -> List[int]:
        if i == len(pattern):
            return prefix
        operation = pattern[i]
        step, limit = 1, 10
        if operation == "D":
            step, limit = -1, 0
        for d in range(prefix[-1] + step, limit, step):
            if d in prefix:
                continue
            prefix.append(d)
            output = Solution.get_permutation(prefix, pattern, i + 1)
            if output != None:
                return output
            prefix.pop()
        return None

    def smallestNumber(self, pattern: str) -> str:
        for i in range(1, 10):
            prefix = [i]
            output = Solution.get_permutation(prefix, pattern, 0)
            if output != None:
                return "".join(map(str, output))
        return ""
