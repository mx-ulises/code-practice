class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        costs = [(1, costs[0]), (7, costs[1]), (30, costs[2])]
        memory = [0]
        for i in range(len(days)):
            memory.append(365000)
            for ticket_legth, cost in costs:
                ticket_start_day = days[i] - ticket_legth + 1
                prev = bisect.bisect_left(days, ticket_start_day)
                memory[-1] = min(memory[-1], memory[prev] + cost)
        return memory[len(days)]
