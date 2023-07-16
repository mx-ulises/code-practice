class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        output[n - 1] = nums[n - 1]
        for i in range(n - 1):
            j = n - i - 1
            output[j - 1] = output[j] * nums[j - 1]
        cummulative = 1
        for i in range(n - 1):
            output[i] = cummulative * output[i + 1]
            cummulative *= nums[i]
        output[n - 1] = cummulative
        return output
