class Solution:
    def binary_search(days: List[int], costs: List[int]) -> int:
        memory = [0]
        for i in range(len(days)):
            memory.append(365000)
            for ticket_legth, cost in costs:
                ticket_start_day = days[i] - ticket_legth + 1
                prev = bisect.bisect_left(days, ticket_start_day)
                memory[-1] = min(memory[-1], memory[prev] + cost)
        return memory[len(days)]

    def using_memory(days: List[int], costs: List[int]) -> int:
        memory = [0] * (days[-1] + 1)
        i = 0
        for day in range(1, len(memory)):
            if day < days[i]:
                memory[day] = memory[day - 1]
            else:
                i += 1
                memory[day] = 365000
                for ticket_legth, cost in costs:
                    ticket_start_day = max(0, day - ticket_legth)
                    memory[day] = min(memory[day], memory[ticket_start_day] + cost)
        return memory[-1]

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        costs = [(1, costs[0]), (7, costs[1]), (30, costs[2])]
        return Solution.using_memory(days, costs)
