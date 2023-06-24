class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        maximum_xor = 0
        for num in nums:
            maximum_xor |= num
        return maximum_xor
