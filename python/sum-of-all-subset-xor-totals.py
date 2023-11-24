class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subset_values = [0]
        total = 0
        for x in nums:
            new_subset_values = []
            for y in subset_values:
                new_subset_values.append(x ^ y)
                total += new_subset_values[-1]
            subset_values.extend(new_subset_values)
        return total
