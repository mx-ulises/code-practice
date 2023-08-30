class Solution:
    def get_non_aritmetic_subsequence(n: int, memory) -> List[int]:
        if n not in memory:
            odds = Solution.get_non_aritmetic_subsequence((n + 1) // 2, memory)
            evens = Solution.get_non_aritmetic_subsequence(n//2, memory)
            memory[n] = [2 * x - 1 for x in odds] + [2 * x for x in evens]
        return memory[n]

    def beautifulArray(self, n: int) -> List[int]:
        return Solution.get_non_aritmetic_subsequence(n, {1: [1]})
