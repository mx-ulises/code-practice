class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        bucket = capacity
        for i in range(len(plants)):
            if bucket < plants[i]:
                steps += i * 2
                bucket = capacity
            bucket -= plants[i]
            steps += 1
        return steps
