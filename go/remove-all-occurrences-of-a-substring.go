func GetPrefixMapper(part string) []int {
    prefixMapper := make([]int, len(part))
    j := 0
    for i := 1; i < len(part); i++ {
        for 0 < j && part[i] != part[j] {
            j = prefixMapper[j - 1]
        }
        if part[i] == part[j] {
            j += 1
        }
        prefixMapper[i] = j
    }
    return prefixMapper
}

func removeOccurrences(s string, part string) string {
    prefixMapper := GetPrefixMapper(part)
    stackIndex := make([]int, 0)
    stackChars := make([]byte, 0)
    j := 0
    for i := 0; i < len(s); i++ {
        c := s[i]
        if 0 < len(stackIndex) {
            j = stackIndex[len(stackIndex) - 1]
        }
        for 0 < j && c != part[j] {
            j = prefixMapper[j - 1]
        }
        if c == part[j] {
            j += 1
        }
        stackIndex = append(stackIndex, j)
        stackChars = append(stackChars, c)
        if j == len(part) {
            stackIndex = stackIndex[:len(stackIndex) - j]
            stackChars = stackChars[:len(stackChars) - j]
            j = 0
        }
    }
    return string(stackChars)
}
