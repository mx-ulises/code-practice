class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        current_population = 0
        maximum_population = 0
        maximum_population_year = -1
        h = []
        for log in logs:
            heappush(h, (log[0], 1))
            heappush(h, (log[1], -1))
        while h:
            year, delta = heappop(h)
            current_population += delta
            while h and h[0][0] == year:
                _, delta = heappop(h)
                current_population += delta
            if maximum_population < current_population:
                maximum_population_year = year
                maximum_population = current_population
        return maximum_population_year
