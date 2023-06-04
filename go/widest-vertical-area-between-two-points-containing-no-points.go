import (
    "sort"
)

func maxWidthOfVerticalArea(points [][]int) int {
    sort.Slice(points, func (i int, j int) bool {
        return points[i][0] < points[j][0]
    })
    maxDiff := 0
    for i := 1; i < len(points); i++ {
        diff := points[i][0] - points[i - 1][0]
        if maxDiff < diff {
            maxDiff = diff
        }
    }
    return maxDiff
}
