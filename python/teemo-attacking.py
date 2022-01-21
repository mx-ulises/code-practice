class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        start = timeSeries[0]
        end = start + duration
        total_duration = 0
        for t in timeSeries:
            if end < t:
                total_duration += end - start
                start = t
            end = t + duration
        total_duration += end - start
        return total_duration
