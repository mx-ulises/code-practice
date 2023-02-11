impl Solution {
    pub fn pivot_integer(n: i32) -> i32 {
        let mut left = 1;
        let mut sum_left = left;
        let mut right = n;
        let mut sum_right = right;
        while left < right {
            if sum_left <= sum_right {
                left += 1;
                sum_left += left;
            } else {
                right -= 1;
                sum_right += right;
            }
        }
        if sum_left == sum_right {
            return left;
        }
        return -1;
    }
}
