class Solution:
    def transit_time(garbage: List[str], travel: List[int], unit_type: str) -> int:
        current_transit_time = 0
        transit_time = 0
        for unit in garbage[0]:
            if unit == unit_type:
                transit_time += 1
        for i in range(len(travel)):
            current_transit_time += travel[i]
            for unit in garbage[i + 1]:
                if unit == unit_type:
                    transit_time += current_transit_time
                    current_transit_time = 0
                    transit_time += 1
        return transit_time

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        minutes = Solution.transit_time(garbage, travel, 'M')
        minutes += Solution.transit_time(garbage, travel, 'P')
        minutes += Solution.transit_time(garbage, travel, 'G')
        return minutes
