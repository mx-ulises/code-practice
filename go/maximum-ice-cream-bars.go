func maxIceCream(costs []int, coins int) int {
	sort.Ints(costs)
	i := 0
	for i < len(costs) && costs[i] <= coins {
		coins -= costs[i]
		i += 1
	}
	return i
}
