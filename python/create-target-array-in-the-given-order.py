class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target_array = []
        n = len(nums)
        for i in range(n):
            #target_array = target_array[:index[i]] + [nums[i]] + target_array[index[i]:]
            target_array.insert(index[i], nums[i])
        return target_array
