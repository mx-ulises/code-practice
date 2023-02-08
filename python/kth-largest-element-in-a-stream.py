class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k
        for x in nums:
            heappush(self.h, x)
            if self.k < len(self.h):
                heappop(self.h)

    def add(self, val: int) -> int:
        heappush(self.h, val)
        if self.k < len(self.h):
            heappop(self.h)
        return self.h[0]
