class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        num = 0
        output = []
        for i in nums:
            num = (num << 1) + i
            output.append(True)
            if num % 5:
                output[-1] = False
        return output
