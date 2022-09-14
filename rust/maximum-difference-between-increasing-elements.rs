use std::cmp;

impl Solution {
    pub fn maximum_difference(nums: Vec<i32>) -> i32 {
        let mut maximal_diff:i32 = -1;
        let mut left:usize = 0;
        let mut right:usize = 1;
        while right < nums.len(){
            if nums[left] < nums[right] {
                maximal_diff = std::cmp::max(maximal_diff, nums[right] - nums[left]);
            } else {
                left = right;
            }
            right += 1; 
        }
        maximal_diff
    }
}
