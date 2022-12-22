MOVES = {
    "N": (1, 0),
    "S": (-1, 0),
    "E": (0, 1),
    "W": (0, -1),
}

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        current = (0, 0)
        visited = set([current])
        for m in path:
            new_position = (current[0] + MOVES[m][0], current[1] + MOVES[m][1])
            if new_position in visited:
                return True
            visited.add(new_position)
            current = new_position
        return False
