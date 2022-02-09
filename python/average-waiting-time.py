class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        if not customers:
            return 0.0
        total_wait_time = 0.0
        n = len(customers)
        current_time = 0
        for customer in customers:
            arrival_time, prep_time = customer
            current_time = max(current_time, arrival_time)
            finish_time = current_time + prep_time
            wait_time = finish_time - arrival_time
            total_wait_time += wait_time
            current_time = finish_time
        return total_wait_time/n
