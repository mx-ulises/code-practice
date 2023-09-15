class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        n = len(arr)
        summatory = [0]
        for x in arr:
            summatory.append(summatory[-1] + x)
        for i in range(n):
            j = i + 1
            while j <= n:
                total += summatory[j] - summatory[i]
                j += 2
        return total
