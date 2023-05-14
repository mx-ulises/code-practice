func minSteps(s string, t string) int {
    offset := int('a')
    var charCount [26]int
    steps := 0
    for i := 0; i < len(s); i++ {
        s_j := int(s[i]) - offset
        charCount[s_j]++
        t_j := int(t[i]) - offset
        charCount[t_j]--
    }
    for i := 0; i < 26; i++ {
        if 0 < charCount[i] {
            steps += charCount[i]
        }
    }
    return steps
}
