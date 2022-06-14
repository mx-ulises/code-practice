class Solution:
    def countElements(self, nums: List[int]) -> int:
        minimal = min(nums)
        maximal = max(nums)
        count = 0
        for x in nums:
            if minimal < x and x < maximal:
                count += 1
        return count        
