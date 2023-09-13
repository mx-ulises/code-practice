class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        mc = 0
        while 1 < len(arr):
            minimal = min(arr)
            i = arr.index(minimal)
            multiplier = 0
            if i == 0:
                multiplier = arr[1]
            elif i == (len(arr) - 1):
                multiplier = arr[-2]
            else:
                multiplier = min(arr[i - 1], arr[i + 1])
            mc += minimal * multiplier
            arr = arr[:i] + arr[i + 1:]
        return mc
