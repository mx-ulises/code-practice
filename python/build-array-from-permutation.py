class Solution:
    def solution_one(nums: List[int]) -> List[int]:
        return [nums[x] for x in nums]

    def solution_two(nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            num = nums[nums[i]] % 1000
            nums[i] += num * 1000
        for i in range(len(nums)):
            nums[i] = nums[i] // 1000
        return nums

    def buildArray(self, nums: List[int]) -> List[int]:
        return Solution.solution_two(nums)
