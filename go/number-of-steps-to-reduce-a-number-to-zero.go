func numberOfSteps(num int) int {
	steps := 0
	for 1 < num {
		steps += 1 + (num & 1)
		num >>= 1
	}
	return steps + num
}
