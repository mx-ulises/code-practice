func partitionLabels(s string) []int {
    char_ranges := make(map[byte][2]int)
    char_order := make([]byte, 0)
    for i := 0; i < len(s); i++ {
        c := s[i]
        old_range, ok := char_ranges[c]
        if !ok {
            char_ranges[c] = [2]int{i, i}
            char_order = append(char_order, c)
        } else {
            char_ranges[c] = [2]int{old_range[0], i}
        }
    }
    output := make([]int, 0)
    output = append(output, char_ranges[char_order[0]][1])
    output_i := 0
    for i:= 0; i < len(char_order); i++ {
        c := char_order[i]
        start, end := char_ranges[c][0], char_ranges[c][1]
        if output[output_i] < start {
            output = append(output, end)
            output_i++
        }
        if output[output_i] < end {
            output[output_i] = end
        }
    }
    current_sum := 0
    for i := 0; i < len(output); i++ {
        output[i] -= (current_sum - 1)
        current_sum += output[i]
    }
    return output
}
