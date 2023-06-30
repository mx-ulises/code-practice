class Solution:
    def find_dupes_memoryless(nums: List[int]) -> List[int]:
        dupes = []
        n = len(nums)
        for i in range(n):
            while nums[i] != 0 and (i + 1) != nums[i] and nums[i] != nums[nums[i] - 1]:
                aux = nums[i]
                nums[i] = nums[nums[i] - 1]
                nums[aux - 1] = aux
            if nums[i] == nums[nums[i] - 1] and (i + 1) != nums[i] and nums[i] != 0:
                dupes.append(nums[i])
                nums[i] = 0
        return dupes

    def find_dupes_memory(nums: List[int]) -> List[int]:
        dupes_map = [-1 for i in range(len(nums))]
        for x in nums:
            dupes_map[x - 1] += 1
        return [i + 1 for i in range(len(nums)) if 0 < dupes_map[i]]

    def findDuplicates(self, nums: List[int]) -> List[int]:
        return Solution.find_dupes_memoryless(nums)
