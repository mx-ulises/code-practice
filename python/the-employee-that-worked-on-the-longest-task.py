class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        current_start_time = 0
        worker_with_longest_working_time = 0
        longest_working_time  = 0
        for (worker_id, leave_time) in logs:
            working_time = leave_time - current_start_time
            if longest_working_time == working_time:
                worker_with_longest_working_time = min(
                    worker_with_longest_working_time,
                    worker_id
                )
            elif longest_working_time < working_time:
                worker_with_longest_working_time = worker_id
                longest_working_time = working_time
            current_start_time = leave_time
        return worker_with_longest_working_time
