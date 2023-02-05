use std::cmp;

impl Solution {
    pub fn max_ascending_sum(nums: Vec<i32>) -> i32 {
        let mut current = nums[0];
        let mut maximal = nums[0];
        for i in 1..nums.len() {
            if nums[i] <= nums[i - 1] {
                current = 0;
            }
            current += nums[i];
            maximal = cmp::max(maximal, current);
        }
        return maximal;
    }
}
