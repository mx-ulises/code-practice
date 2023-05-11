func numOfPairs(nums []string, target string) int {
    len2nums := make(map[int][]string)
    for i := 0; i < len(nums); i++ {
        num := nums[i]
        len2nums[len(num)] = append(len2nums[len(num)], num)
    }
    count := 0
    for len_1, nums_1 := range len2nums {
        len_2 := len(target) - len_1
        nums_2, ok := len2nums[len_2]
        if ok {
            for i := 0; i < len(nums_1); i++ {
                num_1 := nums_1[i]
                i_alt := 0
                if len_1 == len_2 {
                    i_alt = i + 1
                }
                for j := i_alt; j < len(nums_2); j++ {
                    num_2 := nums_2[j]
                    if (num_1 + num_2) == target {
                        count += 1
                    }
                    if len_1 == len_2 && (num_2 + num_1) == target {
                        count += 1
                    }
                }
            }
        }
    }
    return count
}
