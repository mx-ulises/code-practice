func GetMoves(n int, memory map[int]int) int {
	_, ok := memory[n]
	if ok {
		return memory[n]
	}
	minimal := n
	for i := 1; i < n; i++ {
		candidate := GetMoves(n-i, memory) + 1
		if candidate < i {
			candidate = i
		}
		if candidate < minimal {
			minimal = candidate
		}
	}
	memory[n] = minimal
	return memory[n]
}

func twoEggDrop(n int) int {
	memory := make(map[int]int)
	memory[0] = 0
	return GetMoves(n, memory)
}
