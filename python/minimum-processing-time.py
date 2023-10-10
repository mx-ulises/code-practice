CORES = 4

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        maximal = 0
        for i in range(len(processorTime)):
            max_batch_proccess_time = 0
            for j in range(CORES):
                task_process_time = tasks[i * CORES + j]
                max_batch_proccess_time = max(max_batch_proccess_time, task_process_time)
            start_time = processorTime[len(processorTime) - i - 1]
            maximal = max(maximal, start_time + max_batch_proccess_time)
        return maximal
