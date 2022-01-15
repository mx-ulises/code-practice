from collections import defaultdict

def get_permutations(nums_count, permutations, current_permutation, size):
    if len(current_permutation) == size:
        permutations.append(list(current_permutation))
        return
    for num in nums_count:
        if nums_count[num]:
            nums_count[num] -= 1
            current_permutation.append(num)
            get_permutations(nums_count, permutations, current_permutation, size)
            current_permutation.pop()
            nums_count[num] += 1

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums_count = defaultdict(lambda: 0)
        for num in nums:
            nums_count[num] += 1
        permutations = []
        current_permutation = []
        get_permutations(nums_count, permutations, current_permutation, len(nums))
        return permutations
