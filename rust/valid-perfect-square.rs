impl Solution {
    pub fn is_perfect_square(num: i32) -> bool {
        let num = num as i64;
        let mut left = 1;
        let mut right = num;
        while left <= right {
            let mid = left + (right - left) / 2;
            let square = mid * mid;
            if square == num {
                return true;
            } else if square < num {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return num == 1;
    }
}
