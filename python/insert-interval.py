class Solution:

    def merge(interval_1, interval_2):
        return (
                    min(interval_1[0], interval_2[0]),
                    max(interval_1[1], interval_2[1])
                )

    def lt(interval_1, interval_2):
        if interval_1[1] < interval_2[0]:
            return True
        return False

    def mergable(interval_1, interval_2):
        if interval_1[0] <= interval_2[0] and interval_2[0] <= interval_1[1]:
            return True
        if interval_2[0] <= interval_1[0] and interval_1[0] <= interval_2[1]:
            return True
        return False

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        added = False
        if len(intervals) != 0:
            interval = intervals.pop(0)
            if Solution.mergable(interval, newInterval):
                merged_interval = Solution.merge(interval, newInterval)
                new_intervals.append(merged_interval)
                added = True
            elif Solution.lt(newInterval, interval):
                new_intervals.append(newInterval)
                new_intervals.append(interval)
                added = True
            else:
                new_intervals.append(interval)

        while intervals:
            interval = intervals.pop(0)
            if Solution.mergable(interval, new_intervals[-1]):
                new_intervals[-1] = Solution.merge(interval, new_intervals[-1])
            elif not added and Solution.mergable(interval, newInterval):
                merged_interval = merged_interval = Solution.merge(interval, newInterval)
                new_intervals.append(merged_interval)
                added = True
            elif not added and Solution.lt(newInterval, interval):
                new_intervals.append(newInterval)
                new_intervals.append(interval)
                added = True
            else:
                new_intervals.append(interval)

        if not added:
            new_intervals.append(newInterval)
        return new_intervals
