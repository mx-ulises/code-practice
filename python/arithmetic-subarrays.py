class Solution:
    def is_aritmetic_subarray(nums_subarray: List[int]) -> bool:
        if len(nums_subarray) < 2:
            return False
        nums_subarray.sort()
        diff = nums_subarray[1] - nums_subarray[0]
        for i in range(1, len(nums_subarray)):
            if (nums_subarray[i] - nums_subarray[i - 1]) != diff:
                return False
        return True

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        output = []
        for i in range(len(l)):
            start, end = l[i], r[i] + 1
            output.append(Solution.is_aritmetic_subarray(nums[start:end]))
        return output
