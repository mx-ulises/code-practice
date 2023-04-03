class Solution:
    def countPoints(self, rings: str) -> int:
        color = 'E'
        colors_in_rod = defaultdict(lambda: 0)
        for c in rings:
            if color == 'R':
                colors_in_rod[c] |= 1
            if color == 'G':
                colors_in_rod[c] |= 2
            if color == 'B':
                colors_in_rod[c] |= 4
            color = c
        point_count = 0
        for rod in colors_in_rod:
            if colors_in_rod[rod] == 7:
                point_count += 1
        return point_count
