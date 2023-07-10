class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        keys_stack = [0]
        while keys_stack:
            key = keys_stack.pop()
            if key in visited:
                continue
            visited.add(key)
            for new_key in rooms[key]:
                keys_stack.append(new_key)
        return len(visited) == len(rooms)
