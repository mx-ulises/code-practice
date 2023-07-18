class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        num_count = defaultdict(lambda: 0)
        for num in nums:
            num_count[num] += 1
        lonely_numbers = []
        for num in num_count:
            pred = num - 1
            succ = num + 1
            if num_count[num] == 1 and pred not in num_count and succ not in num_count:
                lonely_numbers.append(num)
        return lonely_numbers
