class Solution:
    def check(x: int, y: int, c: int) -> bool:
        return abs(x - y) <= c

    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        triplets = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if Solution.check(arr[i], arr[j], a) == False:
                    continue
                for k in range(j + 1, n):
                    b_check = Solution.check(arr[j], arr[k], b)
                    c_check = Solution.check(arr[i], arr[k], c)
                    if b_check and c_check:
                        triplets += 1
        return triplets
