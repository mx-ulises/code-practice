NBHD = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def get_value(grid, i, j):
    out_boundaries = [-1, len(grid)]
    if i in out_boundaries or j in out_boundaries:
        return 0
    return grid[i][j]


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        sumatory = 0
        for i in range(n):
            for j in range(n):
                v = grid[i][j]
                if v:
                    for nb in NBHD:
                        nb_v = get_value(grid, i + nb[0], j + nb[1])
                        sumatory += max(0, v - nb_v)
                    sumatory += 2
        return sumatory
