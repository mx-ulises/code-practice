class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_nums = {}
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            if y in visited_nums:
                return (visited_nums[y], i)
            visited_nums[x] = i
