func GetPeakDirection(arr []int, i int) int {
	direction := 0
	if i == 0 || arr[i-1] < arr[i] {
		direction += 1
	}
	if i == len(arr)-1 || arr[i] > arr[i+1] {
		direction -= 1
	}
	return direction
}

func peakIndexInMountainArray(arr []int) int {
	left := 0
	right := len(arr) - 1
	mid := (left + right) / 2
	direction := GetPeakDirection(arr, mid)
	for direction != 0 {
		if direction < 0 {
			right = mid - 1
		} else {
			left = mid + 1
		}
		mid = (left + right) / 2
		direction = GetPeakDirection(arr, mid)
	}
	return mid
}
