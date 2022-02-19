class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        current = arr[0]
        count = 1
        maximal = current
        maximal_count = count
        for i in range(1, n):
            if current == arr[i]:
                count += 1
            else:
                current = arr[i]
                count = 1
            if maximal_count <= count:
                maximal = current
                maximal_count = count
        return maximal
