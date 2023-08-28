func bulbSwitch(n int) int {
	i := 1
	bulbCount := 0
	for (i * i) <= n {
		bulbCount += 1
		i += 1
	}
	return bulbCount
}
