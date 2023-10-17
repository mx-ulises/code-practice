func commonFactors(a int, b int) int {
	factors := 0
	minimal := a
	if b < minimal {
		minimal = b
	}
	for i := 1; i <= minimal; i++ {
		if a%i == 0 && b%i == 0 {
			factors += 1
		}
	}
	return factors
}
