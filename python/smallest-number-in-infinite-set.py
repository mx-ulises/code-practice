class SmallestInfiniteSet:

    def __init__(self):
        self.current_minimal = 0
        self.reinsert_heap = []
        self.reinsert_map = {}

    def popSmallest(self) -> int:
        current_minimal = self.current_minimal
        if self.reinsert_heap:
            current_minimal = heappop(self.reinsert_heap)
            del self.reinsert_map[current_minimal]
        else:
            self.current_minimal += 1
        return current_minimal

    def addBack(self, num: int) -> None:
        if num < self.current_minimal and num not in self.reinsert_map:
            heappush(self.reinsert_heap, num)
            self.reinsert_map[num] = True
