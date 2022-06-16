class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.reset()


    def flip(self) -> List[int]:
        #print(self.intervals)
        interval_index = random.randint(0, len(self.intervals) - 1)
        interval = self.intervals[interval_index]
        self.intervals[interval_index] = self.intervals[-1]
        self.intervals.pop()
        current = random.randint(interval[0], interval[1])
        if interval[0] <= current - 1:
            self.intervals.append((interval[0], current - 1))
        if current + 1 <= interval[1]:
            self.intervals.append((current + 1, interval[1]))
        i = current // self.n
        j = current % self.n
        return [i, j]


    def reset(self) -> None:
        self.intervals = [(0, self.m * self.n - 1)]
