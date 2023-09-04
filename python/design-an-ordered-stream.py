class OrderedStream:

    def __init__(self, n: int):
        self.stream = deque([None] * n)
        self.head = 0
        self.size = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1 - self.head] = value
        start = self.head
        output = []
        while self.head < self.size and self.stream[0] != None:
            self.head += 1
            output.append(self.stream.popleft())
        return output

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
