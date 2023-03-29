class Solution:
    def solution_one(n: int, k: int) -> List[List[int]]:
        prefixes = [[]]
        output = []
        for i in range(1, n + 1):
            new_prefixes = list(prefixes)
            for prefix in prefixes:
                new_prefix = list(prefix)
                new_prefix.append(i)
                if len(new_prefix) == k:
                    output.append(new_prefix)
                else:
                    new_prefixes.append(new_prefix)
            prefixes = new_prefixes
        return output


    def get_combination(i: int, n: int, k: int, current: List[int], output: List[List[int]]) -> None:
        if k == len(current):
            output.append(list(current))
        elif n < i:
            return
        else:
            current.append(i)
            Solution.get_combination(i + 1, n, k, current, output)
            current.pop()
            Solution.get_combination(i + 1, n, k, current, output)


    def solution_two(n: int, k: int) -> List[List[int]]:
        output = []
        current = []
        Solution.get_combination(1, n, k, current, output)
        return output


    def combine(self, n: int, k: int) -> List[List[int]]:
        return Solution.solution_two(n, k)
