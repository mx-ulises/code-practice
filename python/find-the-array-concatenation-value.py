class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concatenation_value = 0
        i, j = 0, len(nums) - 1
        while i < j:
            multiplier = 10 ** (int(math.log10(nums[j])) + 1)
            concatenation_value += nums[i] * multiplier + nums[j]
            i += 1
            j -= 1
        if i == j:
            concatenation_value += nums[i]
        return concatenation_value
