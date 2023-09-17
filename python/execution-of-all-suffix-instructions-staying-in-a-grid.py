MOVES = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}

class Solution:
    def is_valid_pos(current_pos: List[int], n: int) -> bool:
        if current_pos[0] < 0 or current_pos[0] == n:
            return False
        if current_pos[1] < 0 or current_pos[1] == n:
            return False
        return True

    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        output = []
        m = len(s)
        for i in range(m):
            current_pos = list(startPos)
            step_count = 0
            for step in range(i, m):
                direction = s[step]
                current_pos[0] += MOVES[direction][0]
                current_pos[1] += MOVES[direction][1]
                if not Solution.is_valid_pos(current_pos, n):
                    break
                step_count += 1
            output.append(step_count)
        return output
