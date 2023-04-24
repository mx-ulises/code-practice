class Solution:
    def get_distance(circle: List[int], point: List[int]) -> float:
        term1 = circle[0] - point[0]
        term2 = term1 * term1
        term3 = circle[1] - point[1]
        term4 = term3 * term3
        return term2 + term4

    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        for circle in queries:
            answer.append(0)
            for point in points:
                r = circle[2] * circle[2]
                d = Solution.get_distance(circle, point)
                if d <= r:
                    answer[-1] += 1
        return answer
