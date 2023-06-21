class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []
        self.increments = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)
            self.increments.append(0)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        increment = self.increments.pop()
        self.increment(len(self.increments), increment)
        return self.stack.pop() + increment

    def increment(self, k: int, val: int) -> None:
        if 0 < len(self.increments):
            increment_index = min(k, len(self.increments)) - 1
            self.increments[increment_index] += val

