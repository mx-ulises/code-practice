class RecentCounter:

    def __init__(self):
        self.dq = Deque()

    def ping(self, t: int) -> int:
        s = t - 3000
        while self.dq and self.dq[0] < s:
            self.dq.popleft()
        self.dq.append(t)
        return len(self.dq)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
