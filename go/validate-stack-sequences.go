func validateStackSequences(pushed []int, popped []int) bool {
	s := make([]int, 0)
	j := 0
	for i := 0; i < len(pushed); i++ {
		s = append(s, pushed[i])
		for 0 < len(s) && s[len(s)-1] == popped[j] {
			s = s[:len(s)-1]
			j += 1
		}
	}
	return len(s) == 0
}
