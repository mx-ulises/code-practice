func SolutionInPlace(s string) string {
	i := 0
	for i < len(s) {
		if s[i] == '*' {
			s = s[:i-1] + s[i+1:]
			i -= 1

		} else {
			i += 1
		}
		fmt.Println(s)
	}
	return s
}

func SolutionStack(s string) string {
	output := make([]rune, 0)
	for _, c := range s {
		if c == '*' {
			output = output[:len(output)-1]
		} else {
			output = append(output, c)
		}
	}
	return string(output)
}

func removeStars(s string) string {
	return SolutionStack(s)
}
