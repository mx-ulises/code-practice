def get_combinations(k, n, prefix, combinations):
    if n < 0:
        return
    if k == 0:
        if n == 0:
            combinations.append(prefix[1:])
        return
    for i in range(prefix[-1] + 1, 10):
        prefix.append(i)
        get_combinations(k - 1, n - i, prefix, combinations)
        prefix.pop()

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        prefix = [0]
        combinations = []
        get_combinations(k, n, prefix, combinations)
        return combinations
