class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        output = 0
        for row in grid:
            row.sort()
        while 0 < len(grid[0]):
            maximal = 0
            for row in grid:
                maximal = max(maximal, row.pop())
            output += maximal
        return output
