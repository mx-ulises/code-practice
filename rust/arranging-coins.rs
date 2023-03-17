impl Solution {
    pub fn arrange_coins(n: i32) -> i32 {
        let mut left = 1;
        let mut right = n;
        while left <= right {
            let mid = (right + left) / 2;
            let complete_rows_coins = mid * (mid + 1) / 2;
            if n == complete_rows_coins {
                return mid;
            } else if n < complete_rows_coins {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return right;
    }
}
