class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        even_array = 0
        odd_array = 0
        fair_array_count = 0
        for i in range(len(nums)):
            if i % 2:
                even_array += nums[i]
            else:
                odd_array += nums[i]
        for i in range(len(nums)):
            if i % 2:
                even_array -= nums[i]
            else:
                odd_array -= nums[i]
            if even_array == odd_array:
                fair_array_count += 1
            if i % 2:
                odd_array += nums[i]
            else:
                even_array += nums[i]
        return fair_array_count
