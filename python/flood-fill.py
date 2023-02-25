DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:
    def is_valid(image: List[List[int]], i, j, color) -> bool:
        if i < 0 or i == len(image):
            return False
        if j < 0 or j == len(image[0]):
            return False
        return image[i][j] == color

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if color == old_color:
            return image
        s = [(sr, sc)]
        while s:
            i, j = s.pop()
            if Solution.is_valid(image, i, j, old_color) == False:
                continue
            image[i][j] = color
            for delta in DIRECTIONS:
                s.append((i + delta[0], j + delta[1]))
        return image
