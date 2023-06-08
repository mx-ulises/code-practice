func GetKeyIndex(ruleKey string) int {
    switch ruleKey {
        case "type": return 0
        case "color": return 1
        case "name": return 2
        default: return -1
    }
}

func countMatches(items [][]string, ruleKey string, ruleValue string) int {
    index := GetKeyIndex(ruleKey)
    matches := 0
    for i := 0; i < len(items); i++ {
        if items[i][index] == ruleValue {
            matches += 1
        }
    }
    return matches
}
