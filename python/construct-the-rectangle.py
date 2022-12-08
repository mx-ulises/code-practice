class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        W = int(sqrt(area))
        while area % W:
            W -= 1
        return [area // W, W]
