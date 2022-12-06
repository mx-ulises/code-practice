class Solution:

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        moves = sum([abs(students[i] - seats[i]) for i in range(len(seats))])
        return moves
