class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = [i + 1 for i in range(len(nums))]
        for i in nums:
            output[i - 1] = 0
        end_of_list = 0
        for i in range(len(output)):
            if output[i] != 0:
                output[end_of_list], output[i] = output[i], output[end_of_list]
                end_of_list += 1
        while output and output[-1] == 0:
            output.pop()
        return output
