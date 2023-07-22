func separateDigits(nums []int) []int {
	output := make([]int, 0)
	for _, num := range nums {
		buffer := make([]int, 0)
		for 0 < num {
			buffer = append(buffer, num%10)
			num /= 10
		}
		for 0 < len(buffer) {
			i := len(buffer) - 1
			output = append(output, buffer[i])
			buffer = buffer[:i]
		}
	}
	return output
}
