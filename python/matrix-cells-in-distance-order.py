MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    def is_valid_position(position: Tuple[int], rows: int, cols: int, visited: Set[int]) -> bool:
        if position in visited:
            return False
        if position[0] < 0 or position[1] < 0:
            return False
        if position[0] == rows or position[1] == cols:
            return False
        return True

    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        output = [(rCenter, cCenter)]
        i = 0
        visited = set(output)
        while i < len(output):
            position = output[i]
            for move in MOVES:
                new_position = (position[0] + move[0], position[1] + move[1])
                if Solution.is_valid_position(new_position, rows, cols, visited):
                    output.append(new_position)
                    visited.add(new_position)
            i += 1
        return output
