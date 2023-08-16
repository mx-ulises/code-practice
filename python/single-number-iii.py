class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        num_1 = 0
        num_2 = 0
        mask = 1
        while (mask & xor) == 0:
            mask = mask << 1
        for num in nums:
            if (mask & num) == 0:
                num_1 ^= num
            else:
                num_2 ^= num
        return [num_1, num_2]
