def get_servers_heap(servers):
    free_servers = []
    for server in range(len(servers)):
        weight = servers[server]
        heappush(free_servers, (weight, server))
    return free_servers

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        m = len(tasks)
        free_servers = get_servers_heap(servers)
        busy_servers = []
        task_queue = []
        task_to_server = [-1] * m
        t = 0
        while t < m or task_queue:
            if t < m:
                duration = tasks[t]
                task_queue.append((t, duration))
            if m <= t and busy_servers:
                t = busy_servers[0][0]
            while busy_servers and busy_servers[0][0] <= t:
                _, weight, server = heappop(busy_servers)
                heappush(free_servers, (weight, server))
            while free_servers and task_queue:
                task, duration = task_queue.pop(0)
                weight, server = heappop(free_servers)
                heappush(busy_servers, (t + duration, weight, server))
                task_to_server[task] = server
            t += 1
        return task_to_server
