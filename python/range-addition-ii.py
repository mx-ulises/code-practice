class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        a_min = m
        b_min = n
        for (a, b) in ops:
            a_min = min(a_min, a)
            b_min = min(b_min, b)
        return a_min * b_min
