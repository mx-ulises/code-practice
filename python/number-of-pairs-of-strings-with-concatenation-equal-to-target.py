class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        lenToNumbers = defaultdict(list)
        while nums:
            num = nums.pop()
            lenToNumbers[len(num)].append(num)
        count = 0
        for len_1 in lenToNumbers:
            len_2 = len(target) - len_1
            if len_2 not in lenToNumbers:
                continue
            while lenToNumbers[len_1]:
                num_1 = lenToNumbers[len_1].pop()
                for num_2 in lenToNumbers[len_2]:
                    if (num_1 + num_2) == target:
                        count += 1
                    if (num_2 + num_1) == target:
                        count += 1
        return count
