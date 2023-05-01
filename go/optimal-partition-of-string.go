func partitionString(s string) int {
    // create an array of size 26 to store the last
    last_char_substring := [26]int{}
    // track number of substrings:
    substrings := 0    
    // Iterate over each byte and add them to the map
    for i := 0; i < len(s); i++ {
		// Get the index in the last_char_substring array
        j := byte(s[i]) - byte('a')
		// If char is in current substring, then increase the substring count
        if last_char_substring[j] == substrings {
            substrings += 1
        }
		// Update the last char substring
        last_char_substring[j] = substrings
    }
	// return count of substrings
    return substrings
}
