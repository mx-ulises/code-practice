OVES = {'U': 1, 'D': -1, "L": 100000, "R": -100000}

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        for c in moves:
            x += MOVES[c]
        return x == 0
