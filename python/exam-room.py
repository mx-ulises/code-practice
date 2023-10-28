class ExamRoom:

    def __init__(self, n: int):
        self.limit = n - 1
        self.memory = []

    def seat(self) -> int:
        if len(self.memory) == 0:
            self.memory.append(0)
            return 0
        position = 0
        distance = self.memory[0]
        for i in range(1, len(self.memory)):
            candidate_distance = (self.memory[i] - self.memory[i - 1]) // 2
            if distance < candidate_distance:
                distance = candidate_distance
                position = self.memory[i - 1] + distance
        candidate_distance = self.limit - self.memory[-1]
        if distance < candidate_distance:
            position = self.limit
        insort(self.memory, position)
        return position

    def leave(self, p: int) -> None:
        i = bisect_left(self.memory, p)
        del self.memory[i]

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
