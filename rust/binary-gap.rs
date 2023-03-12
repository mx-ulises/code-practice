use std::cmp;

impl Solution {
    pub fn binary_gap(mut n: i32) -> i32 {
        while 0 < n && (n & 1) == 0 {
            n = n >> 1;
        }
        let mut max_distance = 0;
        let mut current_distance = 0;
        while 0 < n {
            if (n & 1) == 1 {
                max_distance = cmp::max(max_distance, current_distance);
                current_distance = 0;
            }
            current_distance += 1;
            n = n >> 1;
        }
        return max_distance;
    }
}
