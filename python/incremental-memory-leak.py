class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        output = [-1, -1, -1]
        i = 1
        memory_crash = False
        h = []
        heappush(h, (-memory1, 1))
        heappush(h, (-memory2, 2))
        while not memory_crash:
            available_memory, memory_id = heappop(h)
            new_memory = -available_memory - i
            if new_memory < 0:
                output[0] = i
                output[memory_id] = -available_memory
                available_memory, memory_id = heappop(h)
                output[memory_id] = -available_memory
                memory_crash = True
            else:
                heappush(h, (-new_memory, memory_id))
                i += 1
        return output
