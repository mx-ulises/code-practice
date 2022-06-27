class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        list_count = len(nums)
        num_count = defaultdict(lambda: 0)
        for list_nums in nums:
            for num in list_nums:
                num_count[num] += 1
        intersection = [num for num in num_count if num_count[num] == list_count]
        intersection.sort()
        return intersection
