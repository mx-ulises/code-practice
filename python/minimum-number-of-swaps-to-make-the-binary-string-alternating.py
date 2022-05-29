class Solution:
    def minSwaps(self, s: str) -> int:
        count_1 = 0
        count_0 = 0
        start_0_swaps = 0
        start_1_swaps = 0
        n = len(s)
        for i in range(n):
            c = s[i]
            if c == "0":
                count_0 += 1
                if i % 2 == 0:
                    start_1_swaps += 1
            if c == "1":
                count_1 += 1
                if i % 2 == 0:
                    start_0_swaps += 1
        if 1 < abs(count_0 - count_1):
            return -1
        elif count_0 < count_1:
            return start_1_swaps
        elif count_1 < count_0:
            return start_0_swaps
        else:
            return min(start_1_swaps, start_0_swaps)
