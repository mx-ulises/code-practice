class Solution:
    def binary_search(nums: List[int], x: int) -> int:
        index = bisect_left(nums, x)
        return index < len(nums) and x == nums[index]

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        triplets = 0
        for x in nums:
            if Solution.binary_search(nums, x - diff) and Solution.binary_search(nums, x + diff):
                triplets += 1
        return triplets
