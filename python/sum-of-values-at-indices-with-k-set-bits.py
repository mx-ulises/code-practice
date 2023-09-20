class Solution:
    def get_set_bits(i: int) -> int:
        set_bits = 0
        while i:
            set_bits += i & 1
            i >>= 1
        return set_bits

    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        summatory = 0
        for i in range(len(nums)):
            if Solution.get_set_bits(i) == k:
                summatory += nums[i]
        return summatory
