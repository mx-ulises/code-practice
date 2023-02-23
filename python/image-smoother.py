WINDOW = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 0), (0, 1),
    (1, -1), (1, 0), (1, 1),
]

class Solution:
    def is_valid_point(point: (int, int), n: int, m: int) -> bool:
        i, j = point
        if i < 0 or i == n:
            return False
        if j < 0 or j == m:
            return False
        return True

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n, m = len(img), len(img[0])
        output = []
        for i in range(n):
            output.append([])
            for j in range(m):
                point_count = 0
                point_sum = 0
                for delta in WINDOW:
                    point = (i + delta[0], j + delta[1])
                    if Solution.is_valid_point(point, n, m):
                        point_count += 1
                        point_sum += img[point[0]][point[1]]
                output[i].append(point_sum // point_count)
        return output
