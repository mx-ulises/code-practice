NB = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def is_valid(i, j, grid, visited):
    n, m = len(grid), len(grid[0])
    if (i, j) in visited:
        return False
    if i < 0 or n <= i:
        return False
    if j < 0 or m <= j:
        return False
    if grid[i][j] == 0:
        return False
    return True

def is_border(i, j, grid):
    n, m = len(grid), len(grid[0])
    if i == 0 or j == 0:
        return True
    if i == n - 1 or j == m - 1:
        return True
    return False
    

def get_island(i, j, grid, visited):
    if not is_valid(i, j, grid, visited):
        return False, False, 0
    visited.add((i, j))
    is_island = not is_border(i, j, grid)
    size = 1
    for offset_i, offset_j in NB:
        nb_is_valid, nb_is_island, nb_size = get_island(i + offset_i, j + offset_j, grid, visited)
        if nb_is_valid:
            is_island &= nb_is_island
            size += nb_size
    return True, is_island, size



class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()
        island_size = 0
        for i in range(n):
            for j in range(m):
                is_valid, is_island, size = get_island(i, j, grid, visited)
                if is_island:
                    island_size += size
        return island_size
