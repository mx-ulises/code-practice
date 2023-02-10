use std::collections::HashSet;

impl Solution {
    pub fn distinct_averages(mut nums: Vec<i32>) -> i32 {
        nums.sort();
        let mut averages = HashSet::new();
        for i in 0..(nums.len() / 2) {
            let average = (nums[i] as f64 + nums[nums.len() - i - 1] as f64) / 2.0;
            averages.insert(average.to_string());
        }
        return averages.len() as i32;
    }
}
