use std::cmp;

impl Solution {
    pub fn find_max_average(nums: Vec<i32>, k: i32) -> f64 {
        let mut sum = 0;
        let k_usize = k as usize;
        for i in 0..k_usize {
            sum += nums[i];
        }
        let mut maximal = sum;
        for i in k_usize..nums.len() {
            sum += nums[i] - nums[i - k_usize];
            maximal = cmp::max(sum, maximal);
        }
        return (maximal as f64) / (k as f64);
    }
}
