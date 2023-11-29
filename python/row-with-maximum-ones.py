class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        position = -1
        max_ones = -1
        n = len(mat[0])
        for i in range(len(mat)):
            ones_sum = sum(mat[i])
            if max_ones < ones_sum:
                max_ones = ones_sum
                position = i
            if max_ones == n:
                break
        return (position, max_ones)
