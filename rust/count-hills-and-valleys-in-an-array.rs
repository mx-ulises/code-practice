use std::cmp;

impl Solution {
    pub fn count_hill_valley(nums: Vec<i32>) -> i32 {
        let mut direction = 0;
        let mut count = 0;
        let mut i = 1;
        while i < nums.len() && nums[i - 1] == nums[i] {
            i += 1;
        }
        while i < nums.len() {
            if nums[i - 1] < nums[i] && direction != 1 {
                count += 1;
                direction = 1;
            } else if nums[i] < nums[i - 1] && direction != -1 {
                count += 1;
                direction = -1;
            }
            i += 1;
        }
        return cmp::max(0, count - 1);
    }
}
