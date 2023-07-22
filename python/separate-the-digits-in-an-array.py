class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        output = []
        for num in nums:
            buffer = []
            while 0 < num:
                buffer.append(num % 10)
                num //= 10
            while 0 < len(buffer):
                output.append(buffer.pop())
        return output
