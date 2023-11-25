class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        mask = 1
        output = 0
        maximal = max(nums)
        while mask <= maximal:
            count = 0
            for x in nums:
                if x & mask:
                    count += 1
                if count == k:
                    output += mask
                    break
            mask <<= 1
        return output
