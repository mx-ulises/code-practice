class Solution:
    def is_valid_placement(perm_i, i, perm):
        if perm[i]:
            return False
        return perm_i % i == 0 or i % perm_i == 0

    def build_beautiful_permutation(perm_i, perm):
        if len(perm) == perm_i:
            return 1
        count = 0
        for i in range(1, len(perm)):
            if Solution.is_valid_placement(perm_i, i, perm):
                perm[i] = True
                count += Solution.build_beautiful_permutation(perm_i + 1, perm)
                perm[i] = False
        return count

    def countArrangement(self, n: int) -> int:
        perm = [False] * (n + 1)
        return Solution.build_beautiful_permutation(1, perm)
