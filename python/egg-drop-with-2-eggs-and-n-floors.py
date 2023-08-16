class Solution:
    def get_minimal(n: int, memory) -> int:
        if n in memory:
            return memory[n]
        minimal = n
        for i in range(1, n):
            candidate = max(1 + Solution.get_minimal(n=n - i, memory=memory), i)
            minimal = min(minimal, candidate)
        memory[n] = minimal
        return memory[n]

    def twoEggDrop(self, n: int) -> int:
        return Solution.get_minimal(n=n, memory={0: 0})
