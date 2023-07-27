func GetReverseNum(x int) int {
	reversed := 0
	for 0 < x {
		reversed = (10 * reversed) + (x % 10)
		x /= 10
	}
	return reversed
}

func countDistinctIntegers(nums []int) int {
	visited := make(map[int]bool)
	count := 0
	for _, x := range nums {
		reversed := GetReverseNum(x)
		if visited[x] == false {
			visited[x] = true
			count += 1
		}
		if visited[reversed] == false {
			visited[reversed] = true
			count += 1
		}
	}
	return count
}
