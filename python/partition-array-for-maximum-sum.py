class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        memory = [0] * (n + 1)
        for i in range(n):
            current_maximal = arr[i]
            for j in range(k):
                l = i - j
                if l < 0:
                    break
                current_maximal = max(current_maximal, arr[l])
                candidate = memory[l] + current_maximal * (j + 1)
                memory[i + 1] = max(memory[i + 1], candidate)
        return memory[n]
