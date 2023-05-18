func largestAltitude(gain []int) int {
    currentAltitude := 0
    maximalAltitude := 0
    for i := 0; i < len(gain); i++ {
        currentAltitude += gain[i]
        if maximalAltitude < currentAltitude {
            maximalAltitude = currentAltitude
        }
    }
    return maximalAltitude
}
