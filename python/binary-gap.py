class Solution:
    def binaryGap(self, n: int) -> int:
        while n and n & 1 == 0:
            n = n >> 1
        max_distance = 0
        current_distance = 0
        while n:
            if n & 1 == 1:
                max_distance = max(max_distance, current_distance)
                current_distance = 0
            current_distance += 1
            n = n >> 1
        return max_distance
