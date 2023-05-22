# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Solution:
    def init_spiral_matrix(m: int, n: int) -> List[List[int]]:
        spiral_matrix = []
        for i in range(m):
            spiral_matrix.append([-1] * n)
        return spiral_matrix

    def in_range(i, m):
        return 0 <= i and i < m

    def get_direction_index(i: int, j: int, m: int, n: int, direction_index: int, spiral_matrix: List[List[int]]) -> int:
        direction = DIRECTIONS[direction_index]
        i += direction[0]
        j += direction[1]
        if Solution.in_range(i, m) == False or Solution.in_range(j, n) == False or spiral_matrix[i][j] != -1:
            direction_index = (direction_index + 1) % 4
        return direction_index

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        spiral_matrix = Solution.init_spiral_matrix(m, n)
        i, j = 0, 0
        direction_index = 0
        while head:
            spiral_matrix[i][j] = head.val
            direction_index = Solution.get_direction_index(i, j, m, n, direction_index, spiral_matrix)
            direction = DIRECTIONS[direction_index]
            i += direction[0]
            j += direction[1]
            head = head.next
        return spiral_matrix
