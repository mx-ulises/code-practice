class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[0])
        diff = 0
        for i in range(1, len(points)):
            diff = max(points[i][0] - points[i - 1][0], diff)
        return diff
