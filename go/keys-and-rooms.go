func canVisitAllRooms(rooms [][]int) bool {
	keysStack := make([]int, 0)
	keysStack = append(keysStack, 0)
	visited := make([]bool, len(rooms))
	visited_count := 0
	for 0 < len(keysStack) {
		peak := len(keysStack) - 1
		key := keysStack[peak]
		keysStack = keysStack[:peak]
		if visited[key] {
			continue
		} else {
			visited_count += 1
			visited[key] = true
		}
		for i := 0; i < len(rooms[key]); i++ {
			keysStack = append(keysStack, rooms[key][i])
		}
	}
	return visited_count == len(rooms)
}
