class Solution:
    def maxNonOverlapping(self, X: List[int], target: int) -> int:
        cummulative_map = {0: 0}
        cummulative = 0
        last_end = -1
        sub_arrays_count = 0
        for i in range(len(X)):
            cummulative += X[i]
            if last_end < cummulative_map.get(cummulative - target, -1):
                last_end = i
                sub_arrays_count += 1
            cummulative_map[cummulative] = i + 1
        return sub_arrays_count
