class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        while nums:
            current = nums[-1]
            i = 0
            while len(nums) and nums[-1] == current:
                if i == len(output):
                    output.append([])
                output[i].append(nums.pop())
                i += 1
        return output
