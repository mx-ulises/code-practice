class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        answer = []
        current = (2 ** maximumBit) - 1
        for num in nums:
            current ^= num
        for i in range(len(nums)):
            answer.append(current)
            current ^= nums[-1 - i]
        return answer
