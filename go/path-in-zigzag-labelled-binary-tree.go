func GetTreeLevel(label int) int {
	level := 0
	for 0 < label {
		level += 1
		label /= 2
	}
	return level
}

func GetInverse(value int, level int) int {
	if level <= 1 {
		return 1
	}
	levelMin := 1 << (level - 1)
	levelMax := (levelMin << 1) - 1
	position := (levelMax - value) + levelMin
	return position
}

func GetLabelOrPosition(value int, level int) int {
	if (level & 1) == 0 {
		value = GetInverse(value, level)
	}
	return value
}

func Reverse(path []int) {
	n := len(path) / 2
	for i := 0; i < n; i++ {
		j := len(path) - i - 1
		aux := path[i]
		path[i] = path[j]
		path[j] = aux
	}
}

func pathInZigZagTree(label int) []int {
	level := GetTreeLevel(label)
	path := make([]int, 0)
	for 0 < level {
		path = append(path, label)
		parentPosition := GetLabelOrPosition(label, level) / 2
		level -= 1
		label = GetLabelOrPosition(parentPosition, level)
	}
	Reverse(path)
	return path
}
