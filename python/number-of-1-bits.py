HAMMING_WEIGHT_MAP = {0: 0}

class Solution:
    def get_hamming_weight_with_mem(x):
        if x in HAMMING_WEIGHT_MAP:
            return HAMMING_WEIGHT_MAP[x]
        y = x >> 1
        HAMMING_WEIGHT_MAP[x] = Solution.get_hamming_weight_with_mem(y) + (x % 2)
        return HAMMING_WEIGHT_MAP[x]


    def get_hamming_weight_without_mem(x):
        count = 0
        while x:
            count += (x % 2)
            x = x >> 1
        return count


    def hammingWeight(self, n: int) -> int:
        return Solution.get_hamming_weight_without_mem(n)
