func convertToTitle(columnNumber int) string {
	A := int('A')
	title := make([]byte, 0)
	for 0 < columnNumber {
		charInt := columnNumber%26 - 1
		if charInt < 0 {
			columnNumber -= 1
			charInt = 25
		}
		char := byte(charInt + A)
		title = append([]byte{char}, title...)
		columnNumber /= 26
	}
	return string(title)
}
