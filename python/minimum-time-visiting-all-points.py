class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        distance = 0
        for i in range(1, len(points)):
            diff_x = abs(points[i - 1][0] - points[i][0])
            diff_y = abs(points[i - 1][1] - points[i][1])
            distance += max(diff_x, diff_y)
        return distance
