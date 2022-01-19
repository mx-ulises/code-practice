class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        garden_paths = defaultdict(list)
        garden_colors = [-1 for _ in range(n)]
        all_colors = set([1, 2, 3, 4])
        for path in paths:
            x, y = path
            garden_paths[x - 1].append(y - 1)
            garden_paths[y - 1].append(x - 1)
        for x in range(n):
            colors_taken = [garden_colors[y] for y in garden_paths[x]]
            available_colors = all_colors - set(colors_taken)
            color = list(available_colors)[0]
            garden_colors[x] = color
        return garden_colors
