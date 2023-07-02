func cellsInRange(s string) []string {
	startCol := int(s[0])
	startRow := int(s[1])
	endCol := int(s[3])
	endRow := int(s[4])
	output := make([]string, 0)
	for i := startCol; i <= endCol; i++ {
		for j := startRow; j <= endRow; j++ {
			col := byte(i)
			row := byte(j)
			cell := string([]byte{col, row})
			output = append(output, cell)
		}
	}
	return output
}
