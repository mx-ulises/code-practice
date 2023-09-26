class Solution:
    def get_next_step(x: int, y: int, p: int, q: int, direction: int) -> Tuple[int, int, int]:
        y = y + q * direction
        if p < y:
            y = p + p - y
            direction = -1
        if y < 0:
            y = -y
            direction = 1
        if x == 0:
            x = p
        else:
            x = 0
        return x, y, direction


    def mirrorReflection(self, p: int, q: int) -> int:
        receptors = {
            (p, 0): 0,
            (p, p): 1,
            (0, p): 2,
        }
        x, y, direction = 0, 0, 1
        while True:
            x, y, direction = Solution.get_next_step(x, y, p, q, direction)
            if (x, y) in receptors:
                return receptors[(x, y)]
        return -1
