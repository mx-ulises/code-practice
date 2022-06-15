MOVE = [(1, 0), (0, 1), (-1, 0), (0, -1)]
DIRECTION = {"L": -1, "R": 1}

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, d = 0, 0, 0
        for i in range(4):
            for instruction in instructions:
                if instruction == "G":
                    x += MOVE[d][0]
                    y += MOVE[d][1]
                else:
                    d += DIRECTION[instruction]
                    d %= 4
            if (x, y, d) == (0, 0, 0):
                return True
        return False
