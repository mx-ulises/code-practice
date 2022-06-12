START = 0
END = 1

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        schedule = []
        for event in events:
            start_time, end_time, value = event
            schedule.append((start_time, START, value))
            schedule.append((end_time, END, value))
        schedule.sort()
        best_finished_event = (0, 0)
        maximal_sum = 0
        for event in schedule:
            time, event_type, value = event
            if event_type == START:
                current_sum = value
                if best_finished_event[0] < time:
                    current_sum += best_finished_event[1]
                maximal_sum = max(maximal_sum, current_sum)
            else:
                if best_finished_event[1] < value:
                    best_finished_event = (time, value)
        return maximal_sum
