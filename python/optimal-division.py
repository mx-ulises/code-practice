class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        numerator = str(nums[0])
        if 1 < len(nums):
            tail = nums[1:]
            denominator = "/".join(map(str, tail))
            if 1 < len(tail):
                return "{}/({})".format(numerator, denominator)
            else:
                return "{}/{}".format(numerator, denominator)
        return numerator
