class Solution:
    def merge(interval_1, interval_2):
        return (min(interval_1[0], interval_2[0]), max(interval_1[1], interval_2[1]))

    def mergable(interval_1, interval_2):
        if interval_1[0] <= interval_2[0] and interval_2[0] <= interval_1[1]:
            return True
        if interval_2[0] <= interval_1[0] and interval_1[0] <= interval_2[1]:
            return True
        return False

    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        new_intervals = []
        i = 0
        while i < len(intervals) and intervals[i][1] < new_interval[0]:
            new_intervals.append(intervals[i])
            i += 1
        if new_intervals and Solution.mergable(new_intervals[-1], new_interval):
            new_intervals[-1] = Solution.merge(new_intervals[-1], new_interval)
        else:
            new_intervals.append(new_interval)
        while i < len(intervals) and Solution.mergable(new_intervals[-1], intervals[i]):
            new_intervals[-1] = Solution.merge(new_intervals[-1], intervals[i])
            i += 1
        while i < len(intervals):
            new_intervals.append(intervals[i])
            i += 1
        return new_intervals
