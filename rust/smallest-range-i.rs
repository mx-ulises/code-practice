use std::cmp;

impl Solution {
    pub fn smallest_range_i(nums: Vec<i32>, k: i32) -> i32 {
        let minimal = *nums.iter().min().unwrap() + k;
        let maximal = *nums.iter().max().unwrap() - k;
        return cmp::max(0, maximal - minimal);
    }
}
